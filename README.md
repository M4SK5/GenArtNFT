# GenArtNFT
Smart contract and generation script for a full ERC-721 collection. It allows combining image elements with multiple combinations to create the complete images and accompanying metadata in json format. Includes -

##Contents
1. Python scripts to combine collection image parts and generate json metadata for a full collection.
2. Python shuffle script to randomize collection order while maintaining correct id and metadata.
3. Solidity contract for a ERC-721 

###Contract Overview

Uses OpenZepplin's libraries to implement a basic [ERC-721](https://docs.openzeppelin.com/contracts/4.x/api/token/erc721#ERC721) compatible contract for an NFT collection.
Extends [ERC721Enumerable](https://docs.openzeppelin.com/contracts/4.x/api/token/erc721#ERC721Enumerable) to add querying capabilities by index.

Includes two minting options -
1. ReserveNFTs(count) - Used only by owner to mint NFTs without cost.
2. mintNFTs(count) - A payable function for users to lazy mint new tokens by sending <mintPrice>*<count> value.
  
##Prequisites 

##Usage
