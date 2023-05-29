---
title: Decentraland player documentation
url: /player
---

### Find help about the various topics in each of these sections

<style>
.section-cards-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin: 0 auto;
    padding-top: 30px;
}
  .section-card {
    width: 250px;
    height: 370px;
    border-radius: 8px;
    box-shadow: 0 5px 10px 0 rgba(0,0,0,.24);
    box-sizing: border-box;
    margin-right: 20px;
    padding: 20px;
    text-align: left;
    transition: all .5s ease-in-out
  }

  .section-card:hover {
      box-shadow: 0 10px 20px 0 rgba(0,0,0,.24);
      -webkit-filter: brightness(1.2);
      filter: brightness(1.2);
      margin-top: -20px;
      transition: all .5s ease-in
  }

  .section-card:hover .section-card-cta span {
    font-weight: 700
  }

  .section-card-info {
    color: #fff;
    width: 100%
  }

  .section-card-info h3,.section-card-info p {
    color: #fff
  }

  .section-cards-container a, .section-cards-container a:hover {
    text-decoration: none!important;
  }

  .section-card-info h3 {
    margin: 16px 0;
  }

  .section-card-img {
    width: 100%;
  }

  @media(max-width: 768px) {
    .section-card {
      height:auto;
      margin: 20px 0;
      width: 100%
    }

    .section-card-img {
      display: block;
      margin: auto
    }
  }

</style>
<div class="dcl section medium">
  <p>Find help about the various topics in each of these sections</p>
  <div class="section-cards-container">
    <a href="/player/general/introduction/">
      <div class="section-card" style="background: linear-gradient(212.97deg, rgb(235, 73, 90) 0%, rgb(212, 83, 223) 100%);">
        <img class="section-card-img" src="https://cdn.decentraland.org/@dcl/docs-site/1.0.0-3144676401.commit-a407e4c/player-world.png">
        <div class="section-card-info">
        <h3>World</h3>
        <p>General info for players</p>
        </div>
      </div>
    </a>
    <a href="/player/market/marketplace/">
      <div class="section-card" style="background: linear-gradient(212.97deg, rgb(236, 96, 163) 0%, rgb(212, 83, 223) 100%);">
        <img class="section-card-img" src="https://cdn.decentraland.org/@dcl/docs-site/1.0.0-3144676401.commit-a407e4c/player-market.png">
        <div class="section-card-info">
          <h3>Market</h3>
          <p>Learn how to trade exclusive tokens.</p>
        </div>
      </div>
    </a>
    <a href="/player/blockchain-integration/get-a-wallet/">
      <div class="section-card" style="background: linear-gradient(212.97deg, rgb(57, 42, 168) 0%, rgb(212, 83, 223) 100%);">
        <img class="section-card-img" src="https://cdn.decentraland.org/@dcl/docs-site/1.0.0-3144676401.commit-a407e4c/player-eth.png">
        <div class="section-card-info">
          <h3>Ethereum Essentials</h3>
          <p>Learn how we use the blockchain</p>
        </div>
      </div>
    </a>
  </div>
</div>
