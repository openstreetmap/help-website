+++
type = "question"
title = "tshark doesn&#x27;t seem to like radius"
description = '''I have a capture file that i&#x27;d like to post process a bit and needing to focus on the sub name and framed ip addr in the radius files, but each time i try to filter off specific radius fields i get: RADIUS$ tshark -r radius.cap2 -R &#x27;radius.Framed-Ip-Address&#x27; tshark: &quot;radius.Framed-Ip-Address&quot; is nei...'''
date = "2012-06-20T09:43:00Z"
lastmod = "2012-06-20T15:17:00Z"
weight = 12078
keywords = [ "radius", "tshark", "framed-ip-address" ]
aliases = [ "/questions/12078" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [tshark doesn't seem to like radius](/questions/12078/tshark-doesnt-seem-to-like-radius)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12078-score" class="post-score" title="current number of votes">0</div><span id="post-12078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a capture file that i'd like to post process a bit and needing to focus on the sub name and framed ip addr in the radius files, but each time i try to filter off specific radius fields i get:</p><p>RADIUS$ tshark -r radius.cap2 -R 'radius.Framed-Ip-Address'</p><p>tshark: "radius.Framed-Ip-Address" is neither a field nor a protocol name.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-radius" rel="tag" title="see questions tagged &#39;radius&#39;">radius</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-framed-ip-address" rel="tag" title="see questions tagged &#39;framed-ip-address&#39;">framed-ip-address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '12, 09:43</strong></p><img src="https://secure.gravatar.com/avatar/30b5fe7ccdbafebd27ccb5d5269085d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="deedr&#39;s gravatar image" /><p><span>deedr</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="deedr has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jun '12, 09:52</strong> </span></p></div></div><div id="comments-container-12078" class="comments-container"><span id="12082"></span><div id="comment-12082" class="comment"><div id="post-12082-score" class="comment-score"></div><div class="comment-text"><p>thanks guys!</p></div><div id="comment-12082-info" class="comment-info"><span class="comment-age">(20 Jun '12, 11:27)</span> <span class="comment-user userinfo">deedr</span></div></div></div><div id="comment-tools-12078" class="comment-tools"></div><div class="clear"></div><div id="comment-12078-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12079"></span>

<div id="answer-container-12079" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12079-score" class="post-score" title="current number of votes">1</div><span id="post-12079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="deedr has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Do you mean <code>radius.Framed-IP-Address</code> (note the caps "IP")<br />
</p><p>I don't have any RADIUS traffic to look at - if you have a sample, can you put it on <a href="http://www.cloudshark.org">CloudShark</a> and then post the URL so we can look? It supports the same display filters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '12, 10:20</strong></p><img src="https://secure.gravatar.com/avatar/365cfc3c62b61b2ed219b5d146e8ad3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zachad&#39;s gravatar image" /><p><span>zachad</span><br />
<span class="score" title="331 reputation points">331</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zachad has 3 accepted answers">21%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jun '12, 10:20</strong> </span></p></div></div><div id="comments-container-12079" class="comments-container"></div><div id="comment-tools-12079" class="comment-tools"></div><div class="clear"></div><div id="comment-12079-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12081"></span>

<div id="answer-container-12081" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12081-score" class="post-score" title="current number of votes">2</div><span id="post-12081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please run the following command to find the available (radius) fields in tshark (and wireshark).</p><p>Windows</p><blockquote><p><code>tshark.exe -G fields | find "radius."</code></p></blockquote><p>Unix:</p><blockquote><p><code>tshark -G fields | grep 'radius\.'</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '12, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jun '12, 15:17</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-12081" class="comments-container"><span id="12085"></span><div id="comment-12085" class="comment"><div id="post-12085-score" class="comment-score">1</div><div class="comment-text"><p>...and pipe it to <code>more</code> (or <code>less</code>, if you have it; Ludwig Mies van der Rohe would be proud :-)), as you're going to get several thousands of lines (8,613 lines in the SVN trunk version).</p></div><div id="comment-12085-info" class="comment-info"><span class="comment-age">(20 Jun '12, 15:17)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-12081" class="comment-tools"></div><div class="clear"></div><div id="comment-12081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

