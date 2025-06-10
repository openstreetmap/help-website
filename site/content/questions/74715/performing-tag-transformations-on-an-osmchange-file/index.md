+++
type = "question"
title = "Performing tag transformations on an osmchange file"
description = '''What&#x27;s the best way of performing a tag transformation on a .osc file? With &quot;osmosis&quot; I can do something like: osmosis --read-pbf before.pbf --tag-transform transform_cy.xml --write-pbf after.pbf  (see here for an example). That works fine for pbfs. &quot;osmosis&quot; does support &quot;--read-xml-change&quot; but unf...'''
date = "2020-05-10T17:32:00Z"
lastmod = "2020-05-11T08:21:00Z"
weight = 74715
keywords = [ "osmium", "osc", "osmfilter", "osmchange", "osmosis" ]
aliases = [ "/questions/74715" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Performing tag transformations on an osmchange file](/questions/74715/performing-tag-transformations-on-an-osmchange-file)

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
<span id="post-74715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74715-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What's the best way of performing a tag transformation on a .osc file?</p>
<p>With "osmosis" I can do something like:</p>
<pre><code>osmosis --read-pbf before.pbf --tag-transform transform_cy.xml --write-pbf after.pbf</code></pre>
<p>(see <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/update_render.sh#L190">here</a> for an example).</p>
<p>That works fine for pbfs. "osmosis" does support "--read-xml-change" but unfortunately:</p>
<pre><code>osmosis --read-xml-change before.osc --tag-transform transform_cy.xml --write-xml-change after.osc</code></pre>
<p>gives an error:</p>
<pre><code>org.openstreetmap.osmosis.core.OsmosisRuntimeException: Task 2-tag-transform does not support data provided by default pipe stored at level 1 in the default pipe stack.</code></pre>
<p>suggesting that transformations aren't supported for osmchange files.</p>
<p>"osmfilter" doesn't seem to like osmchange fies at all:</p>
<pre><code>osmfilter before.osc --modify-tags=&quot;name:cy to name&quot; -o=after.osc</code></pre>
<p>gives</p>
<pre><code>osmfilter Warning: unexpected end of input file: before.osc</code></pre>
<p>"osmium" has some <a href="https://osmcode.org/docs.html">documentation</a> but it <a href="https://duckduckgo.com/?q=transform+site%3Ahttps%3A%2F%2Fosmcode.org%2F&amp;t=canonical&amp;ia=web">does not mention</a> tag transformations.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-osc" rel="tag" title="see questions tagged &#39;osc&#39;">osc</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-osmchange" rel="tag" title="see questions tagged &#39;osmchange&#39;">osmchange</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 May '20, 17:32</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-74715" class="comments-container">
<span id="74725"></span>
<div id="comment-74725" class="comment">
<div id="post-74725-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The tongue it cheek answer is "vi" or, automated "sed" :-).</p>
<p>I suppose if any of the tools supports JOSM style OSM .xml format (that is supports negative ids and doesn't bork on the action attribute) you could apply the ocs file, transform the tags, extract the ocs file again.</p>
</div>
<div id="comment-74725-info" class="comment-info">
<span class="comment-age">(11 May '20, 07:36)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74715-form-container" class="comment-form-container">
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

<span id="74727"></span>

<div id="answer-container-74727" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74727-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not a complete answer, but maybe it helps you to get towards a solution:</p>
<ol>
<li>Osmium can transform any OSM file into OPL format and back. The OPL format is a simple text format with one line per OSM object which makes it very easy to do transformations with <code>sed</code> or similiar tools on the command line, or even a small script of your favourite scripting language. The OPL format was specifically designed to allow these kinds of things. For more, see the <a href="https://osmcode.org/opl-file-format/">documentation</a>.</li>
<li>If you like Python, you can use PyOsmium and write a little program to do the transformations.</li>
<li>Unlike Osmosis which handles .osm and .osc files differently, they are handled in the same way in Osmium internally. Only when reading and writing a file it chooses the different format based on the file name suffix. You might be able to "convert" the .osc file into an .osm file and then Osmosis won't notice what it is working on. After that you use Osmium to "convert" it back. That's just an idea, you have to experiment to see whether you can get this to work.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '20, 08:21</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-74727" class="comments-container">
&#10;</div>
<div id="comment-tools-74727" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74727-form-container" class="comment-form-container">
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

