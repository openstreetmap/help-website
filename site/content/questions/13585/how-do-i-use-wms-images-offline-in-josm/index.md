+++
type = "question"
title = "How do I use WMS images offline in JOSM?"
description = '''The JOSM help says this:  To reuse the tiles over JOSM sessions without having the reload them from the server, right click on the WMS layer and set a bookmark. During the next session, select the new WMS created by the bookmark in the WMS memu.  But I don&#x27;t seem to have a &#x27;bookmark&#x27; option in the l...'''
date = "2012-06-18T07:59:00Z"
lastmod = "2016-03-10T21:13:00Z"
weight = 13585
keywords = [ "wms", "josm", "cache" ]
aliases = [ "/questions/13585" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I use WMS images offline in JOSM?](/questions/13585/how-do-i-use-wms-images-offline-in-josm)

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
<span id="post-13585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13585-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The <a href="http://josm.openstreetmap.de/wiki/Help/Menu/Imagery">JOSM help</a> says this:</p>
<blockquote>
<p>To reuse the tiles over JOSM sessions without having the reload them from the server, right click on the WMS layer and set a bookmark. During the next session, select the new WMS created by the bookmark in the WMS memu.</p>
</blockquote>
<p>But I don't seem to <em>have</em> a 'bookmark' option in the layer contextual menu. Am I missing something obvious?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wms" rel="tag" title="see questions tagged &#39;wms&#39;">wms</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-cache" rel="tag" title="see questions tagged &#39;cache&#39;">cache</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jun '12, 07:59</strong></p>
<img src="https://secure.gravatar.com/avatar/51b9455e1dba4db831de473436c989f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="samwilson&#39;s gravatar image" />
<p><span>samwilson</span><br />
<span class="score" title="336 reputation points">336</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="samwilson has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-13585" class="comments-container">
<span id="48617"></span>
<div id="comment-48617" class="comment">
<div id="post-48617-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Anyone find a WMS imagery provider for North America Satellite imagery?</p>
</div>
<div id="comment-48617-info" class="comment-info">
<span class="comment-age">(10 Mar '16, 21:13)</span> <span class="comment-user userinfo">gregcrago</span>
</div>
</div>
</div>
<div id="comment-tools-13585" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13585-form-container" class="comment-form-container">
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

<span id="13742"></span>

<div id="answer-container-13742" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13742-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-13742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="samwilson has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is what the layer context menu looks like for me (in the current stable version 5267):</p>
<p><img src="/upfiles/josm-wms-bookmark.png" alt="Screenshot: JOSM’s WMS layer context menu" /></p>
<p>When using “Set WMS Bookmark” a new entry is added to the “Imagery” menu.</p>
<p>The other possibility should be to use the context menu entries to save to and load the WMS layer from a file. With this all cached tiles and server settings are saved to one huge package file which can be loaded later and on a different machine, too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '12, 14:00</strong></p>
<img src="https://secure.gravatar.com/avatar/97f754e0356a74acc666550948b48bd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hfs&#39;s gravatar image" />
<p><span>hfs</span><br />
<span class="score" title="851 reputation points">851</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hfs has 3 accepted answers">17%</span></p>
</img>
</div>
</div>
<div id="comments-container-13742" class="comments-container">
<span id="14391"></span>
<div id="comment-14391" class="comment">
<div id="post-14391-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. I don't know why, but I'm now getting the same thing. I have updated JOSM since I posted this question, so perhaps something changed; perhaps I'm just blind!</p>
</div>
<div id="comment-14391-info" class="comment-info">
<span class="comment-age">(19 Jul '12, 03:43)</span> <span class="comment-user userinfo">samwilson</span>
</div>
</div>
<span id="14401"></span>
<div id="comment-14401" class="comment">
<div id="post-14401-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Make sure you have WMS layer and not a TMS layer. For TMS there is no need to set a bookmark, but on Linux it may be useful to change the cache path (advanced preference key <code>imagery.tms.tilecache_path</code>), so the cache doesn't get cleared on reboot.</p>
</div>
<div id="comment-14401-info" class="comment-info">
<span class="comment-age">(19 Jul '12, 18:02)</span> <span class="comment-user userinfo">bastik</span>
</div>
</div>
</div>
<div id="comment-tools-13742" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13742-form-container" class="comment-form-container">
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

