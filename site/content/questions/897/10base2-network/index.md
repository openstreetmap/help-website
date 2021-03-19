+++
type = "question"
title = "10base2 network"
description = '''I have a customer that still uses Thinnet (10base2) and has been having issues with his network. There are random crashes. I was hoping to bring in a Windows 2003 Server Box (that&#x27;s all I have) with Wireshark installed and hook it up to the network using a media converter and let it analyze all traf...'''
date = "2010-11-10T08:53:00Z"
lastmod = "2010-11-11T08:36:00Z"
weight = 897
keywords = [ "10base2", "analyze", "thinnet", "network" ]
aliases = [ "/questions/897" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [10base2 network](/questions/897/10base2-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-897-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a customer that still uses Thinnet (10base2) and has been having issues with his network. There are random crashes. I was hoping to bring in a Windows 2003 Server Box (that's all I have) with Wireshark installed and hook it up to the network using a media converter and let it analyze all traffic throughout the week.</p><p>My understanding of 10base2 is limited. But I am assuming it still uses the same protocols. But I wanted to make sure this "solution" won't cause any network issues. Thanks all!</p></div><div id="question-tags" class="tags-container tags">10base2 analyze thinnet network</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '10, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/f1c5cb4cd13f50bb2d93413a40f56c9c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ralphy006&#39;s gravatar image" /><p>ralphy006<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ralphy006 has no accepted answers">0%</span></p></div></div><div id="comments-container-897" class="comments-container"></div><div id="comment-tools-897" class="comment-tools"></div><div class="clear"></div><div id="comment-897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="898"></span>

<div id="answer-container-898" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-898-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>All that 10Base2 affects is the media - thinnet and coax. As long as the adapter you are using can be seen by Wireshark then you can capture traffic. Most likely the network is using a protocol set that Wireshark dissects. Check Help &gt; Supported Protocols in Wireshark to see the list.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '10, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p>lchappell ♦<br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-898" class="comments-container"></div><div id="comment-tools-898" class="comment-tools"></div><div class="clear"></div><div id="comment-898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="912"></span>

<div id="answer-container-912" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-912-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>When troubleshooting 10Base-2 problems, the following list will typically find the "random" crashes.</p><p>1) T connectors with cracks in them. I'm sure no one makes TDRs for 10Base2 anymore so you'll have to visually inspect every one of them. Good luck with that! 2) Terminators that are marginal. You'll probably have to hit ebay to see if you can guy some terminators. If you have a university near by, it may be worth your while to see if any of the network guys have old terminators in their drawers somewhere. Worth a shot. 3) Someone extended the T connector by adding another length of cable. Each T connector must connect directly to the NIC. You can't have a cable running from the NIC to the T connector.</p><p>This is a long shot, but see if anyone is bringing in a hub with 10Base-2 -&gt; 10Base-T conversion built-in. I won't elaborate for now since it's a long shot. If they have something like this, the troubleshooting path will take a different course. For example, Digital used to make a box called DELNI that did this.<br />
</p><p>With the cost of modern day equipment, I cannot believe they are still running thinnet. My last conversion from NW2.2 running Arcnet to Ethernet was late nineties for a Holiday Inn in Wisconsin. <em>IF</em> they decide to convert, make sure you spec PLENTY of time for the conversion. I had to spend an extra night in the HOliday Inn because I forgot how slow NW2.2 and Arcnet was.....grrrr.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '10, 08:36</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></p></div></div><div id="comments-container-912" class="comments-container"><span id="936"></span><div id="comment-936" class="comment"><div id="post-936-score" class="comment-score"></div><div class="comment-text"><p>ARCnet! I love it, Hansang! Remember G-net and Omninet? Eeek - I feel old!</p></div><div id="comment-936-info" class="comment-info"><span class="comment-age">(13 Nov '10, 14:27)</span> lchappell ♦</div></div><span id="970"></span><div id="comment-970" class="comment"><div id="post-970-score" class="comment-score"></div><div class="comment-text"><p>I still remember being floored by how slow it was to copy things. we get spoiled so quickly with newer technology that it's very easy to forget "how it used to be" I still remember telling the manager, "oh the drive is so small it won't take long at all to migrate the data" I had my handy dandy (and trusty) JRB Utilities so I thought I'd be out of there in in no time at all. IT TOOK SO LONG!!!! On their PCs, I was able to type "DIR" and <strong>READ</strong> the lines as it went scrolling by. Unreal that my HTC phone probably has more computing power that our servers from a decade and a half ago.</p></div><div id="comment-970-info" class="comment-info"><span class="comment-age">(15 Nov '10, 20:07)</span> hansangb</div></div><span id="971"></span><div id="comment-971" class="comment"><div id="post-971-score" class="comment-score"></div><div class="comment-text"><p>You guys should write a book or something... ;)</p></div><div id="comment-971-info" class="comment-info"><span class="comment-age">(15 Nov '10, 22:56)</span> Jaap ♦</div></div><span id="980"></span><div id="comment-980" class="comment"><div id="post-980-score" class="comment-score"></div><div class="comment-text"><p>You still run across ARCnet in, of all places, the building automation (think door controls, HVAC, etc.) world...</p><p>I still keep an old 3Com EtherLink PCMCIA in my backpack just because its dongle supports 10Base2 - you never know...</p></div><div id="comment-980-info" class="comment-info"><span class="comment-age">(16 Nov '10, 17:33)</span> wesmorgan1</div></div></div><div id="comment-tools-912" class="comment-tools"></div><div class="clear"></div><div id="comment-912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

