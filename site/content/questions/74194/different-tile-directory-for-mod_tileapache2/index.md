+++
type = "question"
title = "Different tile directory for mod_tile/apache2"
description = '''Hi, I struggle to change the tile directory for the rendering tool chain. I changed /etc/renderd.conf: [renderd]...tile_dir=/data/mod_tile  Renderd saves the tiles in this directory, so that works fine. But apache still seems to try to get the tiles from the default path &quot;/var/lib/mod_tile&quot;. I could...'''
date = "2020-04-14T22:25:00Z"
lastmod = "2020-04-14T23:56:00Z"
weight = 74194
keywords = [ "apache", "renderd", "mod_tile" ]
aliases = [ "/questions/74194" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Different tile directory for mod_tile/apache2](/questions/74194/different-tile-directory-for-mod_tileapache2)

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
<span id="post-74194-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74194-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74194-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I struggle to change the tile directory for the rendering tool chain. I changed /etc/renderd.conf:</p>
<pre><code>[renderd]...tile_dir=/data/mod_tile</code></pre>
<p>Renderd saves the tiles in this directory, so that works fine. But apache still seems to try to get the tiles from the default path "/var/lib/mod_tile". I couldn't find any other setting where to tell apache2 where it can find the tiles.</p>
<p>I also tried to activate the option</p>
<pre><code>AddTileConfig /data/mod_tile/ default</code></pre>
<p>in this file "/etc/apache2/sites-available/tileserver_site.conf". But there is no difference.</p>
<p>The apache2 log file says "Loading tile config default at /osm/ for zooms 0 - 20 from tile directory /var/lib/mod_tile with extension .png and mime type image/png" So somewhere this default tile directory overrides the renderd.conf tile_dir. Does anyone know where I can change this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Apr '20, 22:25</strong></p>
<img src="https://secure.gravatar.com/avatar/537a2599a1104fc0b9d044b8ee6be379?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders2&#39;s gravatar image" />
<p><span>Anders2</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders2 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Apr '20, 23:08</strong> </span></p>
</div>
</div>
<div id="comments-container-74194" class="comments-container">
&#10;</div>
<div id="comment-tools-74194" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74194-form-container" class="comment-form-container">
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

<span id="74197"></span>

<div id="answer-container-74197" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74197-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Found out why. Maybe it helps others to solve a similar problem:</p>
<p>The tile directory must be changed in the [renderd]section and added in the [default] section!</p>
<pre><code>[renderd] ... tile_dir=/data/mod_tile</code></pre>
<p>AND</p>
<pre><code>[default] ... TILEDIR=/data/mod_tile</code></pre>
<p>I think the default /etc/renderd.conf file didn't contain the "TILEDIR=..." so it is not intuitive to add the path to this section as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '20, 23:56</strong></p>
<img src="https://secure.gravatar.com/avatar/537a2599a1104fc0b9d044b8ee6be379?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders2&#39;s gravatar image" />
<p><span>Anders2</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders2 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Apr '20, 00:09</strong> </span></p>
</div>
</div>
<div id="comments-container-74197" class="comments-container">
&#10;</div>
<div id="comment-tools-74197" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74197-form-container" class="comment-form-container">
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

