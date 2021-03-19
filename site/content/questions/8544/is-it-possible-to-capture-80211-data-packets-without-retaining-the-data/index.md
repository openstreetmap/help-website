+++
type = "question"
title = "Is it possible to capture 802.11 data packets without retaining the data?"
description = '''I am presently using Wireshark and the AirPcapNx to capture 802.11 packets. My goal is to be able to analyze operation of the network without retaining the payload data in my capture files. I need header information, so cannot simply filter out entire data packets. I basically need to capture data p...'''
date = "2012-01-22T15:20:00Z"
lastmod = "2012-01-22T17:35:00Z"
weight = 8544
keywords = [ "filter_out_data" ]
aliases = [ "/questions/8544" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to capture 802.11 data packets without retaining the data?](/questions/8544/is-it-possible-to-capture-80211-data-packets-without-retaining-the-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8544-score" class="post-score" title="current number of votes">0</div><span id="post-8544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am presently using Wireshark and the AirPcapNx to capture 802.11 packets. My goal is to be able to analyze operation of the network without retaining the payload data in my capture files. I need header information, so cannot simply filter out entire data packets. I basically need to capture data packets, yet filter out the payload data. Though temporary capture of the data payload information may be necessary for Wireshark to perform packet error detection, I have no need for such data. Any ideas?<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter_out_data" rel="tag" title="see questions tagged &#39;filter_out_data&#39;">filter_out_data</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '12, 15:20</strong></p><img src="https://secure.gravatar.com/avatar/02cf4ed95be4ca7470e1bd5ed538c62d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="S_P&#39;s gravatar image" /><p><span>S_P</span><br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="S_P has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-8544" class="comments-container"></div><div id="comment-tools-8544" class="comment-tools"></div><div class="clear"></div><div id="comment-8544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8545"></span>

<div id="answer-container-8545" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8545-score" class="post-score" title="current number of votes">1</div><span id="post-8545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go ahead and capture like you're used to, and then use <strong>editcap -S</strong> to keep only a specified number of bytes for each packets. It's usually good to keep the minimum at 64 bytes to have headers up to TCP/UDP in there, but you can set anything you like.</p><p>BTW, editcap is installed together with Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '12, 15:24</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-8545" class="comments-container"><span id="8548"></span><div id="comment-8548" class="comment"><div id="post-8548-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Jasper. First time using editcap. I will give it a shot.</p></div><div id="comment-8548-info" class="comment-info"><span class="comment-age">(22 Jan '12, 16:14)</span> <span class="comment-user userinfo">S_P</span></div></div><span id="8549"></span><div id="comment-8549" class="comment"><div id="post-8549-score" class="comment-score"></div><div class="comment-text"><p>Looks like it worked as advertised.<br />
</p><p>Problem is that I need 128 bytes for the beacons, and there are many data frames shorter than 128 bytes.</p><p>I should have been more clear w.r.t. my goal. I want to avoid capturing user-specific payload data. I want to stay as far away from any user's personal communication data as possible (even if they are using MY network). Thanks again for your response. If you have additional advice, please!!!</p></div><div id="comment-8549-info" class="comment-info"><span class="comment-age">(22 Jan '12, 17:00)</span> <span class="comment-user userinfo">S_P</span></div></div><span id="8550"></span><div id="comment-8550" class="comment"><div id="post-8550-score" class="comment-score"></div><div class="comment-text"><p>You can try to use an more advanced trace file editing tool, for example bittwiste (you'll find it on sourceforge). With the -L parameter you can tell it to discard anything beyond a certain layer, for example <strong>bittwiste -I infile -O outfile -L 4</strong> keeps everything up to TCP/UDP.</p><p>Other tools of interest might be tcprewrite and pktanon; I am not sure if any of these will work correctly with WiFi traces though.</p></div><div id="comment-8550-info" class="comment-info"><span class="comment-age">(22 Jan '12, 17:35)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-8545" class="comment-tools"></div><div class="clear"></div><div id="comment-8545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

