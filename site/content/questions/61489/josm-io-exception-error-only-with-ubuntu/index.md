+++
type = "question"
title = "JOSM IO Exception Error only with Ubuntu"
description = '''I&#x27;ve been having a mistake on JOSM for a few weeks now that I do not understand. The problem is only on the Ubuntu version, tested on two different machines and there is the same problem, which makes the downloading and loading of data on OSM very long. On Windows it works by doing the same things. ...'''
date = "2018-01-05T10:22:00Z"
lastmod = "2018-01-12T19:15:00Z"
weight = 61489
keywords = [ "download", "josm", "exception", "io", "error" ]
aliases = [ "/questions/61489" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM IO Exception Error only with Ubuntu](/questions/61489/josm-io-exception-error-only-with-ubuntu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61489-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been having a mistake on JOSM for a few weeks now that I do not understand. The problem is only on the Ubuntu version, tested on two different machines and there is the same problem, which makes the downloading and loading of data on OSM very long. On Windows it works by doing the same things.</p>
<p>JOSM is updated to the latest version. He says this: "IO Exception" The problem hinders me to do data updates in OSM</p>
<p>What can I do?! <img src="/upfiles/Schermata_del_2017-12-22_09-52-38_i0YOpKZ.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-exception" rel="tag" title="see questions tagged &#39;exception&#39;">exception</span> <span class="post-tag tag-link-io" rel="tag" title="see questions tagged &#39;io&#39;">io</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '18, 10:22</strong></p>
<img src="https://secure.gravatar.com/avatar/1d048d920daa7455d4cd2d2304b7f314?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vancori&#39;s gravatar image" />
<p><span>vancori</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vancori has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-61489" class="comments-container">
<span id="61490"></span>
<div id="comment-61490" class="comment">
<div id="post-61490-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Sounds like an IPv6 issue. What's the value of the advanced preference "ipv6.validated" on both machines?</p>
</div>
<div id="comment-61490-info" class="comment-info">
<span class="comment-age">(05 Jan '18, 10:32)</span> <span class="comment-user userinfo">don-vip</span>
</div>
</div>
<span id="61495"></span>
<div id="comment-61495" class="comment">
<div id="post-61495-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The value of "ipv6.validated" is true</p>
</div>
<div id="comment-61495-info" class="comment-info">
<span class="comment-age">(05 Jan '18, 11:23)</span> <span class="comment-user userinfo">vancori</span>
</div>
</div>
</div>
<div id="comment-tools-61489" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61489-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="61496"></span>

<div id="answer-container-61496" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61496-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OK I understood. I changed the parameter "validated.ipv6" from true to false. I did several tests and now it works! I can say the problem is derived that in these weeks I switched from ADSL with an operator, to the optical fiber with a new operator, which has other parameters of navigation for the internet.</p>
<p>Thanks for your kind help! :-)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '18, 12:06</strong></p>
<img src="https://secure.gravatar.com/avatar/1d048d920daa7455d4cd2d2304b7f314?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vancori&#39;s gravatar image" />
<p><span>vancori</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vancori has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61496" class="comments-container">
&#10;</div>
<div id="comment-tools-61496" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61496-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61605"></span>

<div id="answer-container-61605" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61605-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This kind of issues come from broken IPv6 on your ISP network. See <a href="https://josm.openstreetmap.de/ticket/15714">https://josm.openstreetmap.de/ticket/15714</a> for an example with Orange, in France.</p>
<p>The workaround in this case is to disable IPv6 completely by setting <strong><code>prefer.ipv6</code></strong> to <strong><code>false</code></strong> in the expert settings (default is "auto") until the ISP fixes the problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '18, 19:15</strong></p>
<img src="https://secure.gravatar.com/avatar/0daf2db5d576b3fcfbb4f3c0e4c54fa6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="don-vip&#39;s gravatar image" />
<p><span>don-vip</span><br />
<span class="score" title="300 reputation points">300</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="don-vip has 2 accepted answers">33%</span></p>
</div>
</div>
<div id="comments-container-61605" class="comments-container">
&#10;</div>
<div id="comment-tools-61605" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61605-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61497"></span>

<div id="answer-container-61497" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61497-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is another further precaution to add that was missing. Each time the JOSM was restarted, the value false was not retained but returned true. This is because the value "prefer ipv6" should be changed from "auto" to "jvm" It's correct? <a href="http://gis.19327.n8.nabble.com/IPv6-problems-td5863584.html">http://gis.19327.n8.nabble.com/IPv6-problems-td5863584.html</a></p>
<p>I hope now everything is OK</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '18, 16:17</strong></p>
<img src="https://secure.gravatar.com/avatar/1d048d920daa7455d4cd2d2304b7f314?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vancori&#39;s gravatar image" />
<p><span>vancori</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vancori has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61497" class="comments-container">
<span id="61498"></span>
<div id="comment-61498" class="comment">
<div id="post-61498-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As a side note - if something is broken externally to JOSM in the IPV6 world perhaps you might want to disable IPV6 in your network client rather than just in JOSM, since other things likely won't work too?</p>
<p>I've just had to do this because a new ADSL router seems to be assigning an IPV6 default gateway and DNS even though IPV6 is allegedly disabled on the router and my ISP doesn't support it at all.</p>
</div>
<div id="comment-61498-info" class="comment-info">
<span class="comment-age">(05 Jan '18, 17:09)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-61497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61497-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

