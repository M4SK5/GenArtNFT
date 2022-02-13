
//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";

contract M4sk5_Genesys_1024 is ERC721Enumerable, Ownable {
    using SafeMath for uint256;
    using Counters for Counters.Counter;

    Counters.Counter private _tokenCounter;

    uint public constant MAX_SUPPLY = 1024;
    uint public constant MAX_PER_MINT = 4; // Only affects non-owner function mintNFTs

    string public baseTokenURI; // Accessed via internal view from parent _baseURI()
    bool public mintOpen;
    uint public mintPrice;

    constructor(string memory name, string memory symbol, string memory baseURI, uint price) ERC721(name, symbol) {
        setBaseURI(baseURI);
        toggleMintOpen(true);
        require(price > 0, "Mint price cannot be 0.");
        setMintPrice(price); // In Wei
    }

    //Get list of owner's address tokens. External == cheaper than public.
    function tokensOfOwner(address _owner) external view returns (uint[] memory) {

        uint tokenCount = balanceOf(_owner);
        uint[] memory tokenIds = new uint256[](tokenCount); //Create array the size of owner balance.

        for (uint i = 0; i < tokenCount; i++) { //Assign token ids to return array.
            tokenIds[i] = tokenOfOwnerByIndex(_owner, i);
        }
        return tokenIds;
    }

    function setBaseURI(string memory _baseTokenURI) public onlyOwner {
        baseTokenURI = _baseTokenURI;
    }


    function setMintOpen(bool _mintOpen) public onlyOwner {
        mintOpen = _mintOpen;
    }
    
    function setMintPrice(uint _mintPrice) public onlyOwner {
        mintPrice = _mintPrice;
    }
    
    function mintNFTs(uint _count) external payable {
        require(mintOpen == true, "Minting is closed.");
        
        uint totalMinted = _tokenCounter.current();
        require(totalMinted.add(_count) <= MAX_SUPPLY, "Not enough NFTs left!");
        require(_count > 0 && _count <= MAX_PER_MINT, "Max number to mint is 4.");
        require(msg.value >= mintPrice.mul(_count), "Not enough ether to purchase NFTs.");

        for (uint i = 0; i < _count; i++) {
            _mintSingleNFT();
        }
    }

    function reserveNFTs(uint _count) external onlyOwner {
        require(mintOpen == true, "Minting is closed.");
        require(_count > 0 , "Number of NFTs must be positive.");

        uint totalMinted = _tokenCounter.current(); 
        require(totalMinted.add(_count) < MAX_SUPPLY, "Not enough NFTs left. Max 1024.");

        for (uint i = 0; i < _count; i++) {
            _mintSingleNFT();
        }
    }

    function withdraw() external payable onlyOwner {
        uint balance = address(this).balance;
        require(balance > 0, "No ether left to withdraw");

        (bool success, ) = (msg.sender).call{value: balance}("");
        require(success, "Transfer failed.");
    }

    //Used internally to set tokenURI as BASE+ID via public interface tokenURI(uint256 tokenId) from ERC721
    function _baseURI() internal view virtual override returns (string memory) {
        return baseTokenURI;
    }

    //Mints and increments token counter. 
    function _mintSingleNFT() private {
        _safeMint(msg.sender, _tokenCounter.current()); //From OpenZepplin ERC721. Assigns current token id to sender address.
        _tokenCounter.increment();         //The only change of _tokenCounter var in the contract
    }

}
