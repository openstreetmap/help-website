+++
type = "question"
title = "[closed] railway=level_crossing no longer rendered by mapnik?"
description = '''Just realized that I&#x27;m no longer seeing the white circle with a black &quot;X&quot; through it that used to indicate a railway=level_crossing node. I searched trac and the wiki but I don&#x27;t see any mention of this being changed. Has it?'''
date = "2013-08-05T02:19:00Z"
lastmod = "2013-08-06T13:51:00Z"
weight = 24900
keywords = [ "rendering", "mapnik" ]
aliases = [ "/questions/24900" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [\[closed\] railway=level_crossing no longer rendered by mapnik?](/questions/24900/railwaylevel_crossing-no-longer-rendered-by-mapnik)

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
<span id="post-24900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24900-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Just realized that I'm no longer seeing the white circle with a black "X" through it that used to indicate a railway=level_crossing node. I searched trac and the wiki but I don't see any mention of this being changed. Has it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Aug '13, 02:19</strong></p>
<img src="https://secure.gravatar.com/avatar/a5ad728cbc8ae89b774c8c61fbeb20f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OceanVortex&#39;s gravatar image" />
<p><span>OceanVortex</span><br />
<span class="score" title="156 reputation points">156</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OceanVortex has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>06 Aug '13, 13:52</strong> </span></p>
</div>
</div>
<div id="comments-container-24900" class="comments-container">
&#10;</div>
<div id="comment-tools-24900" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24900-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is answered, right answer was accepted" by OceanVortex 06 Aug '13, 13:52

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="24906"></span>

<div id="answer-container-24906" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24906-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="OceanVortex has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As far as I can see the <a href="https://github.com/gravitystorm/openstreetmap-carto">CartoCSS stylesheet</a> currently defines only a rule for <em>railway=crossin</em>g (in <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/amenity-symbols.mss">amenity-symbols.mss</a>), but not for <em>railway=level_crossing</em> (although the image to render is named <em>level_crossing.png</em>). Seems like a bug report is a good idea.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Aug '13, 07:48</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-24906" class="comments-container">
<span id="24917"></span>
<div id="comment-24917" class="comment">
<div id="post-24917-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Yet in project.mml <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/project.mml">https://github.com/gravitystorm/openstreetmap-carto/blob/master/project.mml</a> I only see railway=level_crossing mentioned, not railway=crossing - which might be why I don't see anything rendered for railway=crossing either, so yes bug report here: <a href="https://github.com/gravitystorm/openstreetmap-carto/issues">https://github.com/gravitystorm/openstreetmap-carto/issues</a></p>
</div>
<div id="comment-24917-info" class="comment-info">
<span class="comment-age">(05 Aug '13, 08:57)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="24923"></span>
<div id="comment-24923" class="comment">
<div id="post-24923-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>OK, I submitted <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/94">the bug report</a>.</p>
</div>
<div id="comment-24923-info" class="comment-info">
<span class="comment-age">(05 Aug '13, 14:17)</span> <span class="comment-user userinfo">OceanVortex</span>
</div>
</div>
</div>
<div id="comment-tools-24906" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24906-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24901"></span>

<div id="answer-container-24901" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24901-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-24901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://www.openstreetmap.org/?mlat=50.0369&amp;mlon=8.7982&amp;zoom=14&amp;layers=M">Example</a> where I am quite sure that there was a crossing symbol a few weeks ago but apparently no change in the data (accessing from Germany). I guess(!) it could be related to the switch to <span>Carto</span> (see question <a href="/questions/24687/">how-to-move-labels</a>) and not being intentional, but still maybe not temporary. Co-incidental someone <a href="http://lists.openstreetmap.org/pipermail/talk/2013-August/067794.html">noticed at Aug 3 11:43</a> on the talk mailing list that there was a DNS change for tile accesses from Austria (now to server "<span>tabaluga</span>").</p>
<p>All in all: I would wait a bit (day?) and report it as bug against the carto stylesheet at some point in time, if not somebody knows better.</p>
<p>Update:</p>
<blockquote>
<p>New tile rendering (Live Worldwide): The default OpenStreetMap.org "standard" map was switched cross to a new rendering server setup over the last weekend. the rendering server also uses the new “openstreetmap-carto” stylesheet.</p>
</blockquote>
<p>(Shortened citation from <a href="http://lists.openstreetmap.org/pipermail/talk/2013-August/067802.html">talk mailing list, Aug 5 2013, 13:41</a>)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Aug '13, 03:27</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Aug '13, 15:47</strong> </span></p>
</div>
</div>
<div id="comments-container-24901" class="comments-container">
<span id="24904"></span>
<div id="comment-24904" class="comment">
<div id="post-24904-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yep, same missing crossings here: <a href="https://www.openstreetmap.org/?lat=51.68236&amp;lon=10.10939&amp;zoom=17&amp;layers=M">https://www.openstreetmap.org/?lat=51.68236&amp;lon=10.10939&amp;zoom=17&amp;layers=M</a> (accessed from germany too).</p>
</div>
<div id="comment-24904-info" class="comment-info">
<span class="comment-age">(05 Aug '13, 07:28)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-24901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24901-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24982"></span>

<div id="answer-container-24982" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24982-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OK, apparently it was indeed a typo in the new CartoCSS stylesheet, and it's been <a href="https://github.com/gravitystorm/openstreetmap-carto/pull/98">fixed</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '13, 13:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a5ad728cbc8ae89b774c8c61fbeb20f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OceanVortex&#39;s gravatar image" />
<p><span>OceanVortex</span><br />
<span class="score" title="156 reputation points">156</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OceanVortex has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24982" class="comments-container">
&#10;</div>
<div id="comment-tools-24982" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24982-form-container" class="comment-form-container">
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

