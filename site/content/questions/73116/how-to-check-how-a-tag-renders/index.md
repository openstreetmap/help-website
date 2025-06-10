+++
type = "question"
title = "How to check how a tag renders?"
description = '''Let&#x27;s say the user uses a tag, say craft=sawmill. But it doesn&#x27;t show up on the map. He is not Tagging for the renderer. He simply needs to check if  He simply needs to hit CTRL+F5 even more times, and it will eventually show up. It will never show up.  The way to check even before getting started w...'''
date = "2020-02-17T21:20:00Z"
lastmod = "2020-02-19T14:02:00Z"
weight = 73116
keywords = [ "rendering", "tags" ]
aliases = [ "/questions/73116" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to check how a tag renders?](/questions/73116/how-to-check-how-a-tag-renders)

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
<span id="post-73116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73116-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Let's say the user uses a tag, say craft=sawmill.</p>
<p>But it doesn't show up on the map.</p>
<p>He is not <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">Tagging for the renderer</a>. He simply needs to check if</p>
<ol>
<li>He simply needs to hit CTRL+F5 even more times, and it will eventually show up.</li>
<li>It will never show up.</li>
</ol>
<p>The way to check even before getting started would be to look at the links on <a href="https://wiki.openstreetmap.org/wiki/Tag:craft=sawmill">https://wiki.openstreetmap.org/wiki/Tag:craft=sawmill</a> . Surely one will lead to real live examples where he can see how this tag will render, even before he makes his first edit!</p>
<p>He eventually gets to <a href="https://taginfo.openstreetmap.org/tags/craft=sawmill#map">https://taginfo.openstreetmap.org/tags/craft=sawmill#map</a> where he sees thousands of dots. Unfortunately they are not clickable.</p>
<p>How can he see an example of how a tag renders?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Feb '20, 21:20</strong></p>
<img src="https://secure.gravatar.com/avatar/47edd1ee4d973c50bbe7991bb063d09d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jidanni&#39;s gravatar image" />
<p><span>jidanni</span><br />
<span class="score" title="339 reputation points">339</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jidanni has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Feb '20, 21:22</strong> </span></p>
</div>
</div>
<div id="comments-container-73116" class="comments-container">
&#10;</div>
<div id="comment-tools-73116" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73116-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="73117"></span>

<div id="answer-container-73117" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73117-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73117-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73117-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>How can he see an example of how a tag renders?</p>
</blockquote>
<ol>
<li>Overpsas Turbo</li>
<li><a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a> (<code>craft=</code> is coincidentally being discussed in <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/1697)">https://github.com/gravitystorm/openstreetmap-carto/issues/1697)</a></li>
</ol>
<p>Of course, you can suggest a better tool is needed.</p>
<p>Below is what I feel like being not faithful about user experience on "checking how a tag renders" in your description.:</p>
<blockquote>
<p>He is not Tagging for the renderer. He simply needs to check</p>
</blockquote>
<p>If he is checking this deeply, he will need to know how to use the appropriate sources, tools, and resources to check. While checking the renderer for correct tagging may be quick and dirty, it is not always correct or a replacement for knowing the tags.</p>
<blockquote>
<p>The way to check even before getting started would be to look at the links on <a href="https://wiki.openstreetmap.org/wiki/Tag:craft=sawmill">https://wiki.openstreetmap.org/wiki/Tag:craft=sawmill</a> . Surely one will lead to real live examples where he can see how this tag will render, even before he makes his first edit!</p>
</blockquote>
<p>Including the wiki.</p>
<p>"This article is a stub. You can help OpenStreetMap by expanding it.".</p>
<p>The tag is also "in use" only, like many others.</p>
<blockquote>
<p>He eventually gets to <a href="https://taginfo.openstreetmap.org/tags/craft=sawmill#map">https://taginfo.openstreetmap.org/tags/craft=sawmill#map</a> where he sees thousands of dots. Unfortunately they are not clickable.</p>
</blockquote>
<p>Fortunately, they are not clickable. Such a small and rendered-static image will not be nice otherwise. It is a statistical diagram illustrating distribution, not an interactive "map". These are also used with as many combination of tags.</p>
<p>Fortunaately, there's a "Overpass Turbo" button on the top right corner.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '20, 22:24</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Feb '20, 22:30</strong> </span></p>
</div>
</div>
<div id="comments-container-73117" class="comments-container">
<span id="73137"></span>
<div id="comment-73137" class="comment">
<div id="post-73137-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK. I found the problem is actually with iD, <a href="https://github.com/openstreetmap/iD/issues/7372">https://github.com/openstreetmap/iD/issues/7372</a></p>
</div>
<div id="comment-73137-info" class="comment-info">
<span class="comment-age">(19 Feb '20, 09:52)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
<span id="73141"></span>
<div id="comment-73141" class="comment">
<div id="post-73141-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>I don't see a bug anywhere. You seem to be under the misconception that you directly edit the map displayed on www.openstreetmap.org. You don't. You edit geographical data that map makers use to build a map of their liking. Actually, you yourself are free to build a map that only shows woods and sawmills.</p>
<p>Granted, that could maybe be made a bit clearer when editing in iD (or any other editor) but I don't seem to recall a lot of noise from other mappers around this issue.</p>
</div>
<div id="comment-73141-info" class="comment-info">
<span class="comment-age">(19 Feb '20, 14:02)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-73117" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73117-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73118"></span>

<div id="answer-container-73118" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73118-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Some ideas:</p>
<ul>
<li>OSM wiki pages often contain rendering example images in the infobox (<a href="https://wiki.openstreetmap.org/wiki/Tag:natural%3Dscrub">example</a>). Of course, these are added by hand, so if no image is shown, that may be either because it's not rendered or because no one has added it to the wiki yet.</li>
<li>Taginfo does have a "projects" tab listing the applications/styles supporting a particular tag, and the icon each of them uses for the feature (<a href="https://taginfo.openstreetmap.org/tags/craft=sawmill#projects">example</a>). This works for many projects, but unfortunately, openstreetmap-carto – the "default style" on osm.org – is not yet among them.</li>
<li>You can use Overpass Turbo to look for existing uses of the tag. For tags with few uses, you can follow the "Overpass turbo" link in the top right corner of a Taginfo page. For more common tags, that link will no longer lead to a global search, so make sure you zoom to an area likely to have the kind of feature you're investigating.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '20, 22:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-73118" class="comments-container">
&#10;</div>
<div id="comment-tools-73118" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73118-form-container" class="comment-form-container">
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

