# GenArtNFT
Smart contract and generation scripts for a complete ERC-721 Generative Art NFT collection. 
It allows combining image elements with multiple combinations to create the complete images and accompanying metadata in json format. Includes -

## Contents
1. nftgen.py - Python script to combine collection image parts and generate json metadata for a full collection.
2. shuffle.py - Python script to randomize collection order while maintaining correct id and metadata.
3. M4sk5Minter.sol - Solidity contract for an enumerable ERC-721 compatible NFT collection.

## Contract Overview

Uses OpenZepplin's libraries to implement a basic [ERC-721](https://docs.openzeppelin.com/contracts/4.x/api/token/erc721#ERC721) compatible contract for an NFT collection.
Extends [ERC721Enumerable](https://docs.openzeppelin.com/contracts/4.x/api/token/erc721#ERC721Enumerable) to add querying capabilities by index.

Includes two minting options -
1. ReserveNFTs(count) - Used only by the owner to mint NFTs without cost.
2. mintNFTs(count) - A payable function for users to lazy mint new tokens by sending <mintPrice>*<count> value.
  
## Prequisites 

- Use an IDE such as Remix to compile and interact with the contract. I've deployed a similar version successfully to Eth and Polygon testnets. 
- Python installed with PIL, json and uuid libraries. 
- Image part files devided into category folders.
  
## Usage

Edit all parameters inside Python files.

1. Create an "Image Parts" folder and place the different image components in the subfolder by category.
2. Change the image parts path and names inside nftgen.py - make sure to control the order of the categories in case their layers overlap.
3. Edit any other necessary constants based on your config.
4. nftgen.py will use input parts to generate complete image files with index and uuid, and then add their respective properties to a json file.
5. Copy any necessary config to the shuffle.py script before running. 
6. Run shuffle.py from nftgen.py output folder - it will randomize indexes in the json file as well as for image names (retaining original uuid in file name).

See comments inside script files for further details.
  
