+++
type = "question"
title = "How to read a .pbf file in Python (without reading the whole file at once)?"
description = '''I need to parse a .pbf file in Python, but using apply_file() on PyOsmium handlers is not working well for me and so I want to use apply_buffer(). I don&#x27;t quite know what format is expected from it and documentation on it is lacklustre, but I assume it&#x27;s to be a binary string encompassing a filebloc...'''
date = "2021-10-01T11:53:00Z"
lastmod = "2021-10-01T11:53:00Z"
weight = 82012
keywords = [ "python", "planet", "osm.pbf", "pbf", "parsing" ]
aliases = [ "/questions/82012" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to read a .pbf file in Python (without reading the whole file at once)?](/questions/82012/how-to-read-a-pbf-file-in-python-without-reading-the-whole-file-at-once)

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
<span id="post-82012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82012-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to parse a .pbf file in Python, but using <code>apply_file()</code> on PyOsmium handlers is <a href="https://github.com/osmcode/pyosmium/issues/187">not working well for me</a> and so I want to use <code>apply_buffer()</code>. I don't quite know what format is expected from it and <a href="https://docs.osmcode.org/pyosmium/latest/ref_osmium.html?highlight=apply_buffer#osmium.SimpleHandler.apply_buffer">documentation on it is lacklustre</a>, but I assume it's to be a binary string encompassing a <a href="https://wiki.openstreetmap.org/wiki/PBF_Format#Encoding_OSM_entities_into_fileblocks">fileblock</a>.</p>
<p><strong>The problem is that if I <code>open()</code> a file in Python I don't know of a way to find fileblocks to feed them to PyOsmium.</strong></p>
<p>It might have something to do with using a <a href="https://developers.google.com/protocol-buffers/docs/overview">protocol buffer</a> library, but Google's own tutorial only shows <a href="https://developers.google.com/protocol-buffers/docs/pythontutorial#reading-a-message">how to read a whole file</a> at once. I can't do that, because the files I'm handling are too large for memory (think planet.osm.pbf), so I need to do it piece by piece.</p>
<p>How should I approach this? Am I asking in the right place?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-osm.pbf" rel="tag" title="see questions tagged &#39;osm.pbf&#39;">osm.pbf</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Oct '21, 11:53</strong></p>
<img src="https://secure.gravatar.com/avatar/d089777d2df0dd15dd795f6f274255fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fsaler&#39;s gravatar image" />
<p><span>fsaler</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fsaler has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82012" class="comments-container">
&#10;</div>
<div id="comment-tools-82012" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82012-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

