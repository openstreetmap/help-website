+++
type = "question"
title = "Use different tile style with openstreetmap-tile-server"
description = '''I have downloaded and configured openstreetmap-tile-server from github repository which is just great and works fine with my map. I would like to test different style insead of gravitystorm&#x27;s. I checked the dockerfile and made research over internet to understand how this server works behind the sce...'''
date = "2021-03-09T12:17:00Z"
lastmod = "2021-03-16T16:51:00Z"
weight = 79199
keywords = [ "generate_tiles", "tiles", "switch2osm", "tileserver" ]
aliases = [ "/questions/79199" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Use different tile style with openstreetmap-tile-server](/questions/79199/use-different-tile-style-with-openstreetmap-tile-server)

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
<span id="post-79199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79199-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have downloaded and configured openstreetmap-tile-server from <a href="https://github.com/Overv/openstreetmap-tile-server/blob/master/README.md">github repository</a> which is just great and works fine with my map.<br />
I would like to test different style insead of <a href="https://github.com/gravitystorm/openstreetmap-carto">gravitystorm's</a>. I checked the dockerfile and made research over internet to understand how this server works behind the scene.<br />
What I found - that server install and uses carto to export gravitystorms project.mml into readable mapnik.xml for Mapnik application.<br />
But I have found different interesting <a href="https://github.com/tilery/pianoforte">style</a> which I would like to use with current image.<br />
What I understand by README file- this is whole application to serve tiles, but I would like to get only CSSes styles as it's written in dockerfile with downloading gravitystorm's style. Is it possible to extract CSS styles?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-generate_tiles" rel="tag" title="see questions tagged &#39;generate_tiles&#39;">generate_tiles</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Mar '21, 12:17</strong></p>
<img src="https://secure.gravatar.com/avatar/735ed8c1abf1a1f7b907b78d9594303c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="engopy&#39;s gravatar image" />
<p><span>engopy</span><br />
<span class="score" title="126 reputation points">126</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="engopy has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-79199" class="comments-container">
<span id="79200"></span>
<div id="comment-79200" class="comment">
<div id="post-79200-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are a bunch of questions over at that github repository already - <a href="https://github.com/Overv/openstreetmap-tile-server/search?q=style&amp;type=issues">https://github.com/Overv/openstreetmap-tile-server/search?q=style&amp;type=issues</a> - do any of those help?</p>
<p>In particular <a href="https://github.com/Overv/openstreetmap-tile-server/issues/152">https://github.com/Overv/openstreetmap-tile-server/issues/152</a> suggests a couple of options.</p>
</div>
<div id="comment-79200-info" class="comment-info">
<span class="comment-age">(09 Mar '21, 12:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="79201"></span>
<div id="comment-79201" class="comment">
<div id="post-79201-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>After studying dockerfile I understand I need to generate mapnik.xml with carto and it is fine.</p>
<p>What is curious for me is- how to know which file (form repository I listed in post) should I convert with carto into mapnik.xml? There is no <code>project.mml</code> - in fact there is no <em>.mml file at all. I found file <code>piano.yml</code> which looks like good candidate to be converted but the extension is .yml and it is confusing. I found some of other repositories with no</em> .mml files.</p>
<p>I know I could ask on all repositories separately, but I gues it's a newbie question and it can be obvious for users here.</p>
</div>
<div id="comment-79201-info" class="comment-info">
<span class="comment-age">(09 Mar '21, 13:00)</span> <span class="comment-user userinfo">engopy</span>
</div>
</div>
<span id="79276"></span>
<div id="comment-79276" class="comment">
<div id="post-79276-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If the file lists the layers, it's the right one. <a href="https://github.com/tilery/pianoforte/blob/master/piano.yml">https://github.com/tilery/pianoforte/blob/master/piano.yml</a> is indeed the right one.</p>
</div>
<div id="comment-79276-info" class="comment-info">
<span class="comment-age">(15 Mar '21, 20:32)</span> <span class="comment-user userinfo">Marcos Dione</span>
</div>
</div>
<span id="79277"></span>
<div id="comment-79277" class="comment">
<div id="post-79277-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>See laso: <a href="/questions/65257/how-to-convert-yml-to-mml-file">https://help.openstreetmap.org/questions/65257/how-to-convert-yml-to-mml-file</a></p>
</div>
<div id="comment-79277-info" class="comment-info">
<span class="comment-age">(15 Mar '21, 20:35)</span> <span class="comment-user userinfo">Marcos Dione</span>
</div>
</div>
<span id="79302"></span>
<div id="comment-79302" class="comment">
<div id="post-79302-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>At the end I have forked openstreetmap-carto repository and with kosmtik I've edited official style to my custom. Than during build OSM docker image I've changed style download path to my repository. It works fine.</p>
</div>
<div id="comment-79302-info" class="comment-info">
<span class="comment-age">(16 Mar '21, 16:51)</span> <span class="comment-user userinfo">engopy</span>
</div>
</div>
</div>
<div id="comment-tools-79199" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79199-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

