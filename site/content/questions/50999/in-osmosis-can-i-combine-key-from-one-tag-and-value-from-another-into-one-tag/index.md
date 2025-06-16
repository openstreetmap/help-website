+++
type = "question"
title = "In Osmosis, can I combine key from one tag and value from another into one tag"
description = '''I have some external data which I&#x27;ve converted into .osm format, resulting in the following:  &amp;lt;tag k=&quot;Mode&quot; v=&quot;highway&quot; /&amp;gt;  &amp;lt;tag k=&quot;Type&quot; v=&quot;primary&quot; /&amp;gt;   which I&#x27;d like to turn into:  &amp;lt;tag k=&quot;highway&quot; v=&quot;primary&quot; /&amp;gt;   (Before anyone asks, this is not for data that will result in a...'''
date = "2016-07-20T16:25:00Z"
lastmod = "2016-07-20T16:56:00Z"
weight = 50999
keywords = [ "osmosis" ]
aliases = [ "/questions/50999" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [In Osmosis, can I combine key from one tag and value from another into one tag](/questions/50999/in-osmosis-can-i-combine-key-from-one-tag-and-value-from-another-into-one-tag)

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
<span id="post-50999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50999-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have some external data which I've converted into .osm format, resulting in the following:</p>
<pre><code>          &lt;tag k=&quot;Mode&quot; v=&quot;highway&quot; /&gt;
          &lt;tag k=&quot;Type&quot; v=&quot;primary&quot; /&gt;</code></pre>
<p>which I'd like to turn into:</p>
<pre><code>          &lt;tag k=&quot;highway&quot; v=&quot;primary&quot; /&gt;</code></pre>
<p>(Before anyone asks, this is <em>not</em> for data that will result in any kind of importing into OSM! Am merely using the OSM toolchain, but with data coming from a shapefile.)</p>
<p>I can't work out from the <a href="https://wiki.openstreetmap.org/wiki/Osmosis/TagTransform#Specifying_a_transform">Osmosis Tag transform documentation</a> how to do this, if it is even possible.</p>
<p>I suppose I am thinking something along these lines, but this doesn't work:</p>
<pre><code>      &lt;translation&gt;
        &lt;name&gt;Convert from Shapefile headings to OSM key-value pairs&lt;/name&gt;
        &lt;description&gt;-&lt;/description&gt;
        &lt;match type=&quot;way&quot;&gt;
          &lt;tag k=&quot;Mode&quot; v=&quot;(.+)&quot; match_id=&quot;kv&quot; /&gt;
          &lt;tag k=&quot;Type&quot; v=&quot;(.+)&quot; match_id=&quot;kv&quot; /&gt;
        &lt;/match&gt;
        &lt;output&gt;
          &lt;copy-unmatched /&gt;
          &lt;tag from_match=&quot;kv&quot; k=&quot;{1}&quot; v=&quot;{2}&quot; /&gt;
        &lt;/output&gt;
      &lt;/translation&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jul '16, 16:25</strong></p>
<img src="https://secure.gravatar.com/avatar/354d4e3cc1b448abb29eb4f1bbac395c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fooquency&#39;s gravatar image" />
<p><span>fooquency</span><br />
<span class="score" title="76 reputation points">76</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fooquency has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jul '16, 16:32</strong> </span></p>
</div>
</div>
<div id="comments-container-50999" class="comments-container">
<span id="51000"></span>
<div id="comment-51000" class="comment">
<div id="post-51000-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've no idea what you want to do with it after osmosis, but if the answer was "load it into a rendering database" note that osm2pgsql can do what you want via a lua script:</p>
<p><a href="https://github.com/openstreetmap/osm2pgsql/blob/master/docs/lua.md">https://github.com/openstreetmap/osm2pgsql/blob/master/docs/lua.md</a></p>
</div>
<div id="comment-51000-info" class="comment-info">
<span class="comment-age">(20 Jul '16, 16:56)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50999" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50999-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

