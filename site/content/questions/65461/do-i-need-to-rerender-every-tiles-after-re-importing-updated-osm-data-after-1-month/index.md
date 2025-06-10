+++
type = "question"
title = "Do I need to rerender every tiles after re-importing updated osm data after 1 month?"
description = '''I prerender osm tiles upto 13 zoom level in my tile server using renderd_list as lower zoom level takes much time for rendering . I don&#x27;t need daily or minutely updates. But I want to make a full planet import to my database once in a 1 month, Do I need to rerender every zoom level again from 0 upto...'''
date = "2018-08-20T09:28:00Z"
lastmod = "2018-08-20T19:19:00Z"
weight = 65461
keywords = [ "openstreetmap", "renderd", "osmosis", "mod_tile" ]
aliases = [ "/questions/65461" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Do I need to rerender every tiles after re-importing updated osm data after 1 month?](/questions/65461/do-i-need-to-rerender-every-tiles-after-re-importing-updated-osm-data-after-1-month)

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
<span id="post-65461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65461-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I prerender osm tiles upto 13 zoom level in my tile server using renderd_list as lower zoom level takes much time for rendering . I don't need daily or minutely updates. But I want to make a full planet import to my database once in a 1 month, Do I need to rerender every zoom level again from 0 upto 13 using renderd_list? Is there any alternative solution?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Aug '18, 09:28</strong></p>
<img src="https://secure.gravatar.com/avatar/943a788b771da12a63057582fbf250b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anuranpal&#39;s gravatar image" />
<p><span>anuranpal</span><br />
<span class="score" title="21 reputation points">21</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anuranpal has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Aug '18, 09:55</strong> </span></p>
</div>
</div>
<div id="comments-container-65461" class="comments-container">
<span id="65462"></span>
<div id="comment-65462" class="comment">
<div id="post-65462-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There's no detail about software used here, so:</p>
<p>1) If someone requests a tile that is quite old, will whatever software you're using rerender it, perhaps in the background? mod_tile, renderd would by default FWIW.</p>
<p>2) Do you change the map style that you are using regularly enough that you'd want to rerender low zoom tiles anyway?</p>
<p>3) Do you apply hourly or minutely updates to your database?</p>
</div>
<div id="comment-65462-info" class="comment-info">
<span class="comment-age">(20 Aug '18, 09:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="65463"></span>
<div id="comment-65463" class="comment">
<div id="post-65463-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. Updated the question, <a href="https://help.openstreetmap.org/users/387/someoneelse"></a><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a></p>
</div>
<div id="comment-65463-info" class="comment-info">
<span class="comment-age">(20 Aug '18, 09:56)</span> <span class="comment-user userinfo">anuranpal</span>
</div>
</div>
</div>
<div id="comment-tools-65461" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65461-form-container" class="comment-form-container">
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

<span id="65476"></span>

<div id="answer-container-65476" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65476-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When a request is made for an old tile, the old tile should be sent to the user and a rendering request will also be made. You can see the "START" and "DONE" messages for tiles by doing this:</p>
<pre><code>sudo tail -f /var/log/syslog | grep &quot; TILE &quot;</code></pre>
<p>What you should see when a user requests an old tile is:</p>
<ol>
<li>The old tile is sent to the requester.</li>
<li>You see "START TILE" and "DONE TILE" messages in syslog for an up-to-date version of that tile.</li>
</ol>
<p>The next time a user requests that tile they'll get the new one, not the old one.</p>
<p>What this means is that if you're happy to serve old tiles the first time a user (re)requests them, then don't run <code>render_list</code>. If you're not, do. Running <code>render_list</code> (perhaps even only for some zoom levels) allows you to have tiles ready for users and render them at a time when your server is not busy.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '18, 19:19</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-65476" class="comments-container">
&#10;</div>
<div id="comment-tools-65476" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65476-form-container" class="comment-form-container">
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

