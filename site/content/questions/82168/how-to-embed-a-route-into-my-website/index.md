+++
type = "question"
title = "How to embed a route into my website?"
description = '''Hi there, when I put how to get between two points and I insert it on my website, the route cannot be seen, I see the empty map without the route that I previously traced, can you help me?'''
date = "2021-10-14T14:13:00Z"
lastmod = "2021-10-17T17:19:00Z"
weight = 82168
keywords = [ "embed", "route" ]
aliases = [ "/questions/82168" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to embed a route into my website?](/questions/82168/how-to-embed-a-route-into-my-website)

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
<span id="post-82168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82168-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there, when I put how to get between two points and I insert it on my website, the route cannot be seen, I see the empty map without the route that I previously traced, can you help me?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-embed" rel="tag" title="see questions tagged &#39;embed&#39;">embed</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Oct '21, 14:13</strong></p>
<img src="https://secure.gravatar.com/avatar/7b9fd8c46625632ce88c9f4ab0757d54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edwinvalencia05&#39;s gravatar image" />
<p><span>edwinvalencia05</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edwinvalencia05 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> converted to question <strong>15 Oct '21, 19:52</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-82168" class="comments-container">
&#10;</div>
<div id="comment-tools-82168" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82168-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="82204"></span>

<div id="answer-container-82204" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82204-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>AFAIK, you can't do that with openstreetmap.org.</p>
<p>It seems to be possible with facilmap, here is the <a href="https://docs.facilmap.org/developers/embed.html">doc</a> to embed a custom map in your website.</p>
<p>Some routers might offer the same functionality, but I don't know.</p>
<p>Otherwise, you could just export the route as GPX, using the router of your choice, and then display that GPX on top of a map (there's a number of <a href="https://leafletjs.com/plugins.html#overlay-data-formats">leaflet plugins</a> to do just that).</p>
<p>Calling a routing service at each visit on your website for a route that never changes seems a bit overkill.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '21, 17:19</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-82204" class="comments-container">
&#10;</div>
<div id="comment-tools-82204" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82204-form-container" class="comment-form-container">
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

