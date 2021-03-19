+++
type = "question"
title = "Convert temporary colors to coloring rule"
description = '''Hi, I have a packet capture with several related TCP connections, all interwoven. And I have used the awesome feature to color each of the connections separately (Ctl-1, Ctl-2, etc.). It works like a charm to see how the connections interact. I have used 5 different colors in all.  Now, if I underst...'''
date = "2016-11-09T16:25:00Z"
lastmod = "2016-11-10T02:52:00Z"
weight = 57231
keywords = [ "colors", "temporary" ]
aliases = [ "/questions/57231" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Convert temporary colors to coloring rule](/questions/57231/convert-temporary-colors-to-coloring-rule)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57231-score" class="post-score" title="current number of votes">0</div><span id="post-57231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a packet capture with several related TCP connections, all interwoven. And I have used the awesome feature to color each of the connections separately (Ctl-1, Ctl-2, etc.). It works like a charm to see how the connections interact. I have used 5 different colors in all.<br />
</p><p>Now, if I understand correctly, these are temporary colors, which will disappear when I close this file. But now I want to make these colors permanent, so I can save this file and send it to a colleague.</p><p>Is there a quick way to turn each of these temporary connection colors into coloring rules, that will live on?</p><p>Thx!<br />
feenyman99</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-colors" rel="tag" title="see questions tagged &#39;colors&#39;">colors</span> <span class="post-tag tag-link-temporary" rel="tag" title="see questions tagged &#39;temporary&#39;">temporary</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '16, 16:25</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p><span>feenyman99</span><br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span> </br></br></p></div></div><div id="comments-container-57231" class="comments-container"></div><div id="comment-tools-57231" class="comment-tools"></div><div class="clear"></div><div id="comment-57231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="57233"></span>

<div id="answer-container-57233" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57233-score" class="post-score" title="current number of votes">0</div><span id="post-57233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="feenyman99 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Coloring rules are specific to your installation of Wireshark. Even if you create coloring rules, they will not travel with the file when you send it to your colleague.</p><p>Why not just send a note with the trace file telling your colleague how to apply temporary coloring and which conversations to apply coloring to?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '16, 17:47</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-57233" class="comments-container"><span id="57236"></span><div id="comment-57236" class="comment"><div id="post-57236-score" class="comment-score">1</div><div class="comment-text"><p>Or setup a profile, setup colouring rules based on tcp.stream and send the profile along with the capture.</p></div><div id="comment-57236-info" class="comment-info"><span class="comment-age">(09 Nov '16, 22:15)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-57233" class="comment-tools"></div><div class="clear"></div><div id="comment-57233-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57249"></span>

<div id="answer-container-57249" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57249-score" class="post-score" title="current number of votes">0</div><span id="post-57249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi</p><p>As Jim says, color rules are specific to your customization of Wireshark. However, you can do a "trick"</p><p>In your Wireshark, go to %appdata%\Wireshark There you have a file called "colorfilters". You can save that file (or send it to anyone else). If you reinstall or install Wireshark in another machine, you just need to copy the file again and open Wireshark.</p><p>Disclaimer: This is not supported by Wireshark and will overwrite all other settings for colors made in Wireshark if the file already exists. Do it at your own risk</p><p>Cheers, Osito</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '16, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/0e9b510379013638f59658b49d7d38cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="osito&#39;s gravatar image" /><p><span>osito</span><br />
<span class="score" title="0 reputation points">0</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="osito has one accepted answer">50%</span></p></div></div><div id="comments-container-57249" class="comments-container"></div><div id="comment-tools-57249" class="comment-tools"></div><div class="clear"></div><div id="comment-57249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

