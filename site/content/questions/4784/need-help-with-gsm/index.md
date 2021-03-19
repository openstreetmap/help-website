+++
type = "question"
title = "Need help with gsm"
description = '''Hello, I&#x27;m new to this software, i&#x27;ve tried to connect my mobile phone to wireshark by the audio/power plug but the mobile did not appear at the interface, now i&#x27;m looking for some documentation in this website i find wireshark used only for ehternet switching networks or WLAN networks?  thank you f...'''
date = "2011-06-28T08:26:00Z"
lastmod = "2011-10-30T05:36:00Z"
weight = 4784
keywords = [ "mobile", "gsm" ]
aliases = [ "/questions/4784" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Need help with gsm](/questions/4784/need-help-with-gsm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4784-score" class="post-score" title="current number of votes">0</div><span id="post-4784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm new to this software, i've tried to connect my mobile phone to wireshark by the audio/power plug but the mobile did not appear at the interface, now i'm looking for some documentation in this website i find wireshark used only for ehternet switching networks or WLAN networks?</p><p>thank you for your time</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mobile" rel="tag" title="see questions tagged &#39;mobile&#39;">mobile</span> <span class="post-tag tag-link-gsm" rel="tag" title="see questions tagged &#39;gsm&#39;">gsm</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '11, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/c000c8e826a06e609abd531060c8f79d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Youssef%20Naki&#39;s gravatar image" /><p><span>Youssef Naki</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Youssef Naki has no accepted answers">0%</span></p></div></div><div id="comments-container-4784" class="comments-container"><span id="4785"></span><div id="comment-4785" class="comment"><div id="post-4785-score" class="comment-score"></div><div class="comment-text"><p>do i need to specify a new interface ?</p></div><div id="comment-4785-info" class="comment-info"><span class="comment-age">(28 Jun '11, 08:39)</span> <span class="comment-user userinfo">Youssef Naki</span></div></div><span id="4791"></span><div id="comment-4791" class="comment"><div id="post-4791-score" class="comment-score"></div><div class="comment-text"><p>What are you trying to do?</p><p>Do you want to capture the raw GSM over-the-air data?</p></div><div id="comment-4791-info" class="comment-info"><span class="comment-age">(28 Jun '11, 10:59)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="6077"></span><div id="comment-6077" class="comment"><div id="post-6077-score" class="comment-score"></div><div class="comment-text"><p>hi again ! sorry for the late reply !!!</p><p>Yes i want to capture DTAP and other signalling packets by using my phone LG GW525 , can you help me ?</p><p>sincerly yours</p></div><div id="comment-6077-info" class="comment-info"><span class="comment-age">(04 Sep '11, 17:39)</span> <span class="comment-user userinfo">Youssef Naki</span></div></div></div><div id="comment-tools-4784" class="comment-tools"></div><div class="clear"></div><div id="comment-4784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6080"></span>

<div id="answer-container-6080" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6080-score" class="post-score" title="current number of votes">2</div><span id="post-6080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, most mobile phones don't support capturing raw GSM/UMTS/cdmaOne/CDMA2000/LTE/WiMAX/etc. traffic. That's why you didn't find anything about using Wireshark for that purpose - there's very little that can be done to capture that traffic, and none of it is integrated with libpcap/WinPcap for Wireshark to use.</p><p>One project to capture GSM traffic is <a href="https://svn.berlin.ccc.de/projects/airprobe/">AirProbe</a>. However, it requires <a href="http://www.ettus.com/products">special software-defined radio hardware</a> and the <a href="http://gnuradio.org/redmine/projects/gnuradio/wiki">GNU Radio</a> software to drive it. I couldn't find anything about using an LG GW525 to sniff GSM/UMTS traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '11, 18:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-6080" class="comments-container"><span id="7154"></span><div id="comment-7154" class="comment"><div id="post-7154-score" class="comment-score"></div><div class="comment-text"><p>Hi Harris</p><p>Sorry for my late reply (again!:( :s ) Thank you so much for your help</p><p>i've found a project runned by a German guy (welte harald) he's working on a project called OpenBTS anyway he's working with Airprobe and Motorola cell phone model c123 with linux, i'll try this and let you know of my results</p><p>kindly</p><p>[converted to a comment]</p></div><div id="comment-7154-info" class="comment-info"><span class="comment-age">(30 Oct '11, 05:36)</span> <span class="comment-user userinfo">Youssef Naki</span></div></div></div><div id="comment-tools-6080" class="comment-tools"></div><div class="clear"></div><div id="comment-6080-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

