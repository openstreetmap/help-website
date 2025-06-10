+++
type = "question"
title = "How do i change background in ID editor to &#x27;OS open map local&#x27;?"
description = '''&#x27;OS open data streetview&#x27; is listed, but according to wiki, that one has been discontinued. The newer alternative is apparently &#x27;OS open map local&#x27;, and its ok to use in OSM. So how do i set it up?'''
date = "2020-11-11T22:21:00Z"
lastmod = "2020-11-12T11:15:00Z"
weight = 77518
keywords = [ "ideditor", "opendata", "imagery", "background", "uk" ]
aliases = [ "/questions/77518" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do i change background in ID editor to 'OS open map local'?](/questions/77518/how-do-i-change-background-in-id-editor-to-os-open-map-local)

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
<span id="post-77518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77518-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-77518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>'OS open data streetview' is listed, but according to wiki, that one has been discontinued. The newer alternative is apparently 'OS open map local', and its ok to use in OSM. So how do i set it up?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-opendata" rel="tag" title="see questions tagged &#39;opendata&#39;">opendata</span> <span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span> <span class="post-tag tag-link-background" rel="tag" title="see questions tagged &#39;background&#39;">background</span> <span class="post-tag tag-link-uk" rel="tag" title="see questions tagged &#39;uk&#39;">uk</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Nov '20, 22:21</strong></p>
<img src="https://secure.gravatar.com/avatar/542b61b423371741b1fac10b365f7c57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LazyLeague&#39;s gravatar image" />
<p><span>LazyLeague</span><br />
<span class="score" title="83 reputation points">83</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LazyLeague has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77518" class="comments-container">
&#10;</div>
<div id="comment-tools-77518" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77518-form-container" class="comment-form-container">
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

<span id="77521"></span>

<div id="answer-container-77521" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77521-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In iD, click on background settings (or use B shortcut), click on ... next to Custom, and use this URL</p>
<pre><code>https://{switch:a,b,c}.os.openstreetmap.org/layer/gb_os_om_local_2020_04/{zoom}/{x}/{y}.png</code></pre>
<p>which I got by checking where <a href="https://os.openstreetmap.org"></a><a href="https://os.openstreetmap.org">https://os.openstreetmap.org</a> was loading the tiles from. Being on an openstreetmap.org server I'm assuming it is OK to use in this way.</p>
<p>Edit: strangely what I'm seeing as the iD background seems to have different building renderings to what I'm seeing at os.openstreetmap.org which I can't explain.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Nov '20, 11:15</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Nov '20, 11:23</strong> </span></p>
</div>
</div>
<div id="comments-container-77521" class="comments-container">
&#10;</div>
<div id="comment-tools-77521" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77521-form-container" class="comment-form-container">
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

