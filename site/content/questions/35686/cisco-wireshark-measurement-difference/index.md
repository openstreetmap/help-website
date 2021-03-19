+++
type = "question"
title = "Cisco &amp; Wireshark measurement difference"
description = '''Hi guys. The first image is showing Bandwidth &amp;amp; Delay advertised by EIGRP Update message sent to other side over se 0/0 and captured by Wireshark. The second one shows Bandwidth &amp;amp; Delay for interface se 0/0, reported by &quot;show interface&quot; command. my question is; why those different??what&#x27;s th...'''
date = "2014-08-23T12:18:00Z"
lastmod = "2014-08-24T11:03:00Z"
weight = 35686
keywords = [ "delay", "bandwidth" ]
aliases = [ "/questions/35686" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Cisco & Wireshark measurement difference](/questions/35686/cisco-wireshark-measurement-difference)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35686-score" class="post-score" title="current number of votes">0</div><span id="post-35686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys. The first image is showing Bandwidth &amp; Delay advertised by EIGRP Update message sent to other side over se 0/0 and captured by Wireshark. The second one shows Bandwidth &amp; Delay for interface se 0/0, reported by "show interface" command. my question is; why those different??what's the scale for Bw &amp; Dly in wireshark?? <img src="https://osqa-ask.wireshark.org/upfiles/img2_1.PNG" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/img1.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-delay" rel="tag" title="see questions tagged &#39;delay&#39;">delay</span> <span class="post-tag tag-link-bandwidth" rel="tag" title="see questions tagged &#39;bandwidth&#39;">bandwidth</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Aug '14, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/db00b14e3649ef46f9c87cb77617ea12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="M_Bazgir&#39;s gravatar image" /><p><span>M_Bazgir</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="M_Bazgir has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Aug '14, 20:47</strong> </span></p></div></div><div id="comments-container-35686" class="comments-container"></div><div id="comment-tools-35686" class="comment-tools"></div><div class="clear"></div><div id="comment-35686-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35688"></span>

<div id="answer-container-35688" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35688-score" class="post-score" title="current number of votes">2</div><span id="post-35688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="M_Bazgir has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>According to the master source code the packet details are as follows:</p><pre><code> * Dissect the TLV Versions 1.2 (legacy) and 3.0 (deprecated) metric
 * sections. The following represents the format
 *
 *    0                   1                   2                   3
 *    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
 *   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 *   |                       Scaled Delay                            |
 *   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 *   |                    Scaled Bandwidth                           |
 *   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 *   |         MTU                                    |   Hopcount   |
 *   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 *   | Reliability  |      Load     |  Internal Tag   |    Flag      |
 *   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+</code></pre><p>So both the Scaled Delay and Scaled Bandwidth are dissected as big endian 32 bit values directly from the packet.</p><p>The delay field, as you can see if you select the field and look at the full field info in the status bar, is in "39.1 nanosec interments". So, 512000 * 39.1 nS = 20019.2 uS.</p><p>For the bandwidth field, the field info says it is in "units of 1Kbit/sec", but I can't think of a way to make the field value of 1657856 come out to 1544 KBit unless it's maybe counting for extra serial bits, e.g. start\stop\parity.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '14, 02:11</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Aug '14, 10:33</strong> </span></p></div></div><div id="comments-container-35688" class="comments-container"><span id="35691"></span><div id="comment-35691" class="comment"><div id="post-35691-score" class="comment-score"></div><div class="comment-text"><p>That's my answer,great. but I think you should pay more attention to your mathematical skills, because "512000*39.1 nS = 20019.92 uS " ;-) thanks alot.</p></div><div id="comment-35691-info" class="comment-info"><span class="comment-age">(24 Aug '14, 06:02)</span> <span class="comment-user userinfo">M_Bazgir</span></div></div><span id="35692"></span><div id="comment-35692" class="comment"><div id="post-35692-score" class="comment-score"></div><div class="comment-text"><p>Looks more like a typo to me, plus you should accept Grahams answer with the check mark button to make it clear to others ;-)</p></div><div id="comment-35692-info" class="comment-info"><span class="comment-age">(24 Aug '14, 09:41)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="35694"></span><div id="comment-35694" class="comment"><div id="post-35694-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@M_Bazgir</span></p><p>It was a typo, both Windows calculator and <a href="https://www.google.com/webhp?ion=1&amp;espv=2&amp;ie=UTF-8#q=39.1ns+*+512000">Google</a> agree the answer is 20019.2us. I've amended the answer.</p></div><div id="comment-35694-info" class="comment-info"><span class="comment-age">(24 Aug '14, 10:33)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="35696"></span><div id="comment-35696" class="comment"><div id="post-35696-score" class="comment-score"></div><div class="comment-text"><p><span>@Jasper</span> thanks for your mention. ;-) I did it. :)</p></div><div id="comment-35696-info" class="comment-info"><span class="comment-age">(24 Aug '14, 11:00)</span> <span class="comment-user userinfo">M_Bazgir</span></div></div><span id="35697"></span><div id="comment-35697" class="comment"><div id="post-35697-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span> Again thanks, your answer was so perfect.</p></div><div id="comment-35697-info" class="comment-info"><span class="comment-age">(24 Aug '14, 11:03)</span> <span class="comment-user userinfo">M_Bazgir</span></div></div></div><div id="comment-tools-35688" class="comment-tools"></div><div class="clear"></div><div id="comment-35688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

