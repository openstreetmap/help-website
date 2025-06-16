+++
type = "question"
title = "What is or how to decide Valid HTTP User-Agent application &quot;name&quot; to avoid OSM Blockage?"
description = '''We are using OSM in our application using ThinkGeo dll. As per OSM policy, we have to use Valid HTTP User-Agent in our application.So I wanted to know how to decide the valid name for the application so that OSM will identify our application is valid and will not block us.  If OSM block any applicat...'''
date = "2020-07-15T10:51:00Z"
lastmod = "2020-07-16T08:03:00Z"
weight = 75718
keywords = [ "valid", "http", "user-agent" ]
aliases = [ "/questions/75718" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is or how to decide Valid HTTP User-Agent application "name" to avoid OSM Blockage?](/questions/75718/what-is-or-how-to-decide-valid-http-user-agent-application-name-to-avoid-osm-blockage)

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
<span id="post-75718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75718-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We are using OSM in our application using ThinkGeo dll. As per OSM policy, we have to use Valid HTTP User-Agent in our application.So I wanted to know how to decide the valid name for the application so that OSM will identify our application is valid and will not block us.</p>
<ol>
<li>If OSM block any application and after how much time OSM will unblock that application</li>
<li>How OSM identify particular application is valid or not based on HTTP User-Agent name?</li>
<li>What is best practice for giving name for Valid HTTP User-Agent?</li>
<li>Can we add company website to easily identify the application in HTTP User-Agent?</li>
</ol>
<p><a href="https://operations.osmfoundation.org/policies/tiles/">https://operations.osmfoundation.org/policies/tiles/</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-valid" rel="tag" title="see questions tagged &#39;valid&#39;">valid</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-user-agent" rel="tag" title="see questions tagged &#39;user-agent&#39;">user-agent</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jul '20, 10:51</strong></p>
<img src="https://secure.gravatar.com/avatar/3d9b989785995a44bbb91888df7f0b28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ashish_Walke&#39;s gravatar image" />
<p><span>Ashish_Walke</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ashish_Walke has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jul '20, 18:20</strong> </span></p>
</div>
</div>
<div id="comments-container-75718" class="comments-container">
<span id="75726"></span>
<div id="comment-75726" class="comment">
<div id="post-75726-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>See also <a href="/questions/75719/how-to-measure-the-heavy-use-of-osm-as-per-osm-policy">https://help.openstreetmap.org/questions/75719/how-to-measure-the-heavy-use-of-osm-as-per-osm-policy</a></p>
</div>
<div id="comment-75726-info" class="comment-info">
<span class="comment-age">(15 Jul '20, 15:20)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-75718" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75718-form-container" class="comment-form-container">
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

<span id="75742"></span>

<div id="answer-container-75742" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75742-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-75742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>1. If OSM block any application and after how much time OSM will unblock that application</code></pre>
<p>That depends. I guess there are no general rules for how long to block a particular application. In the worst case your application will get blocked forever.</p>
<pre><code>2. How OSM identify particular application is valid or not based on HTTP User-Agent name?</code></pre>
<p>There is a <del>black list</del> deny list for "bad" applications. Everything else is allowed.</p>
<pre><code>3. What is best practice for giving name for Valid HTTP User-Agent?</code></pre>
<p>Choose a unique name, ideally including the version of your application.</p>
<pre><code>4. Can we add company website to easily identify the application in HTTP User-Agent?</code></pre>
<p>This is not necessary. A unique name is enough to identify your application and the corresponding website.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '20, 08:03</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-75742" class="comments-container">
&#10;</div>
<div id="comment-tools-75742" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75742-form-container" class="comment-form-container">
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

