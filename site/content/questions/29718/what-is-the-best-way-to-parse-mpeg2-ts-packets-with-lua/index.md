+++
type = "question"
title = "What is the best way to parse MPEG2 TS packets with Lua"
description = '''I would like to capture IP stream and then parse MPEG2 TS incapsulated in it, i need to findout CC counters/errors, PCR etc. function tap.packet(pinfo,tvb, calls every IP packet, can i change it to every TS packet?'''
date = "2014-02-11T13:51:00Z"
lastmod = "2014-02-26T08:16:00Z"
weight = 29718
keywords = [ "lua", "mpegts" ]
aliases = [ "/questions/29718" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is the best way to parse MPEG2 TS packets with Lua](/questions/29718/what-is-the-best-way-to-parse-mpeg2-ts-packets-with-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29718-score" class="post-score" title="current number of votes">0</div><span id="post-29718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to capture IP stream and then parse MPEG2 TS incapsulated in it, i need to findout CC counters/errors, PCR etc. function tap.packet(pinfo,tvb, calls every IP packet, can i change it to every TS packet?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-mpegts" rel="tag" title="see questions tagged &#39;mpegts&#39;">mpegts</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '14, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/d0b5db4f049ef0f56f66df48b4c46f8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vovka_morkovka&#39;s gravatar image" /><p><span>vovka_morkovka</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vovka_morkovka has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>26 Feb '14, 22:03</strong> </span></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-29718" class="comments-container"></div><div id="comment-tools-29718" class="comment-tools"></div><div class="clear"></div><div id="comment-29718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29941"></span>

<div id="answer-container-29941" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29941-score" class="post-score" title="current number of votes">1</div><span id="post-29941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try this:</p><p><code>local tap = Listener.new("ip","mp2t")</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '14, 11:39</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-29941" class="comments-container"><span id="30092"></span><div id="comment-30092" class="comment"><div id="post-30092-score" class="comment-score"></div><div class="comment-text"><p>but it will enter to function tap.packet(pinfo,tvb) every IP packet not every TS packet as i would expect, correct?</p></div><div id="comment-30092-info" class="comment-info"><span class="comment-age">(21 Feb '14, 18:13)</span> <span class="comment-user userinfo">vovka_morkovka</span></div></div><span id="30095"></span><div id="comment-30095" class="comment"><div id="post-30095-score" class="comment-score"></div><div class="comment-text"><p>Well I haven't tried it, since I don't have a capture file handy with TS packets and non-TS packets, but in theory it should only call tap.packet() for packets matching the filter in that second argument to Listener.new(), and thus only MPEG2 TS packets.</p></div><div id="comment-30095-info" class="comment-info"><span class="comment-age">(21 Feb '14, 19:25)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="30197"></span><div id="comment-30197" class="comment"><div id="post-30197-score" class="comment-score"></div><div class="comment-text"><p>I have tested and it does not work as expected. I can send you capture if you want.</p></div><div id="comment-30197-info" class="comment-info"><span class="comment-age">(26 Feb '14, 00:39)</span> <span class="comment-user userinfo">vovka_morkovka</span></div></div><span id="30205"></span><div id="comment-30205" class="comment"><div id="post-30205-score" class="comment-score"></div><div class="comment-text"><p><span>@vovka_morkovka</span></p><p>Your "answers" have been converted to comments as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-30205-info" class="comment-info"><span class="comment-age">(26 Feb '14, 02:13)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="30207"></span><div id="comment-30207" class="comment"><div id="post-30207-score" class="comment-score"></div><div class="comment-text"><p>Yes please send it - or put it up on cloudshark, or attach it to a new bugzilla ticket (<a href="https://bugs.wireshark.org/bugzilla/)">https://bugs.wireshark.org/bugzilla/)</a></p></div><div id="comment-30207-info" class="comment-info"><span class="comment-age">(26 Feb '14, 08:16)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-29941" class="comment-tools"></div><div class="clear"></div><div id="comment-29941-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

