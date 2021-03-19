+++
type = "question"
title = "Analyze PCAP file"
description = '''Hello - sorry if this is beating a dead horse. I have 2 PCAP files captured during a write between two hosts. I am needing someone to look at these PCAP files and help analyze them and possibly see where the issue lies. Long story short - we are only achieving about 20% BW on 10GB local LAN pipe. An...'''
date = "2014-03-26T08:19:00Z"
lastmod = "2014-03-27T14:45:00Z"
weight = 31175
keywords = [ "pcap", "analysis" ]
aliases = [ "/questions/31175" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Analyze PCAP file](/questions/31175/analyze-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31175-score" class="post-score" title="current number of votes">0</div><span id="post-31175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello - sorry if this is beating a dead horse. I have 2 PCAP files captured during a write between two hosts. I am needing someone to look at these PCAP files and help analyze them and possibly see where the issue lies. Long story short - we are only achieving about 20% BW on 10GB local LAN pipe. Any suggestions for a newbie would be great.</p><p>Thanks for you time.</p><p>CM</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '14, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/8a6d9fcda84edaa7cd891d0c22726d79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chrissezhi&#39;s gravatar image" /><p><span>chrissezhi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chrissezhi has no accepted answers">0%</span></p></div></div><div id="comments-container-31175" class="comments-container"></div><div id="comment-tools-31175" class="comment-tools"></div><div class="clear"></div><div id="comment-31175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31180"></span>

<div id="answer-container-31180" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31180-score" class="post-score" title="current number of votes">0</div><span id="post-31180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>well, I don't think that someone here will be able/willing to look at two capture files taken on <strong>10GB</strong> links, as that's quite a lot of data and a time consuming task. How would you even provide those capture files for download??</p><p>I think it's better to look for a networking guru in your 'neighborhood' who is able to check your capture files and your network setup.</p><p>We can (probably) <strong>help you</strong> to look at the capture files <strong>yourself</strong>.</p><p>To start with some simple things first:</p><ul><li>how do you know it's only 20% BW?</li><li>how did you create the capture file?</li><li>how did you ensure that the capture system did not drop frames due to 'overload'?</li><li>what kind of application is that?</li><li>did you enable jumbo frames on you network equipment and servers?</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '14, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Mar '14, 08:54</strong> </span></p></div></div><div id="comments-container-31180" class="comments-container"><span id="31185"></span><div id="comment-31185" class="comment"><div id="post-31185-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt for the reply.</p><p>The setup was as followings. Used Lan Speed Test to write a 10GB file from host a to host b. In Wireshark, I filter the capture to only listen for Host A to Host B. Ran the test and stopped the capture.</p><p>Only 20% - because I can not get over 2GB when looking at performance. Via Wireshark Not sure, that is what I was hoping to find out. Using LAN Speed Test - simple write file. No Jumbo Frames.</p></div><div id="comment-31185-info" class="comment-info"><span class="comment-age">(26 Mar '14, 09:05)</span> <span class="comment-user userinfo">chrissezhi</span></div></div><span id="31187"></span><div id="comment-31187" class="comment"><div id="post-31187-score" class="comment-score"></div><div class="comment-text"><p>so, the 20% is a metric printed by Wireshark?</p></div><div id="comment-31187-info" class="comment-info"><span class="comment-age">(26 Mar '14, 09:07)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-31180" class="comment-tools"></div><div class="clear"></div><div id="comment-31180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31240"></span>

<div id="answer-container-31240" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31240-score" class="post-score" title="current number of votes">0</div><span id="post-31240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With TCP you have a maximum possible troughput between two hosts regardless of the bandwith. In the packet capture look at the Window Size and Round Trip Time of the connection and use the link below to calculate the maximum troughput and optimal TCP buffer size:</p><p><a href="https://www.switch.ch/network/tools/tcp_throughput/index.html">https://www.switch.ch/network/tools/tcp_throughput/index.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '14, 14:45</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-31240" class="comments-container"></div><div id="comment-tools-31240" class="comment-tools"></div><div class="clear"></div><div id="comment-31240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

