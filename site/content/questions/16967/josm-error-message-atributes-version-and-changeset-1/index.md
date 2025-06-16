+++
type = "question"
title = "[closed] JOSM error message: &quot;Atributes version and changeset = -1&quot;"
description = '''I have :   installed Rails Port downloaded OSM data from http://download.bbbike.org/osm/ imported a country with Osmosis on my PostgreSQL server  I want to :  change things with JOSM  But :  When I want to download map data from my OSM server with JOSM, JOSM reports an error:   Failed to download da...'''
date = "2012-10-17T17:26:00Z"
lastmod = "2017-05-18T23:30:00Z"
weight = 16967
keywords = [ "josm", "port", "rails" ]
aliases = [ "/questions/16967" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] JOSM error message: "Atributes version and changeset = -1"](/questions/16967/josm-error-message-atributes-version-and-changeset-1)

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
<span id="post-16967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16967-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-16967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have :</p>
<ul>
<li>installed Rails Port</li>
<li>downloaded OSM data from <a href="http://download.bbbike.org/osm/">http://download.bbbike.org/osm/</a></li>
<li>imported a country with Osmosis on my PostgreSQL server</li>
</ul>
<p>I want to :</p>
<ul>
<li>change things with JOSM</li>
</ul>
<p>But :</p>
<ul>
<li>When I want to download map data from my OSM server with JOSM, JOSM reports an error:</li>
</ul>
<blockquote>
<p>Failed to download data. Its format is either unsupported, ill-formed, and/or inconsistent. Details (untranslated): Illegal value for attribute 'version' on OSM primitive with ID 26616418. Got -1. (at line 4, column 128)</p>
</blockquote>
<p>Here is an extract from the map.osm that JOSM tries to import :</p>
<pre><code>&lt;node id=&quot;65262752&quot; version=&quot;-1&quot; changeset=&quot;-1&quot; lat=&quot;36.76644&quot; lon=&quot;3.06899&quot; visible=&quot;true&quot; timestamp=&quot;1970-01-01T00:59:59Z&quot;&gt;</code></pre>
<p>What's going wrong here?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-rails" rel="tag" title="see questions tagged &#39;rails&#39;">rails</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Oct '12, 17:26</strong></p>
<img src="https://secure.gravatar.com/avatar/7b617cf420f8c250aa7020faf6919bd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lucciniolo&#39;s gravatar image" />
<p><span>Lucciniolo</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lucciniolo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>18 May '17, 23:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-16967" class="comments-container">
<span id="16981"></span>
<div id="comment-16981" class="comment">
<div id="post-16981-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In fact, all vesion and changeset of the .osm that i have imported was equal to -1 !</p>
<p>I think that it is not normal. What do you think about that ?</p>
</div>
<div id="comment-16981-info" class="comment-info">
<span class="comment-age">(17 Oct '12, 21:20)</span> <span class="comment-user userinfo">Lucciniolo</span>
</div>
</div>
<span id="16983"></span>
<div id="comment-16983" class="comment">
<div id="post-16983-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok. In fact, it is normal because I dowmload tne data on <a href="http://download.bbbike.org/osm/">http://download.bbbike.org/osm/</a> which have not diffs.</p>
<p>What can i do to use my database with JOSM ?</p>
<p>Can i change version and changeset manuelly ?</p>
</div>
<div id="comment-16983-info" class="comment-info">
<span class="comment-age">(17 Oct '12, 21:29)</span> <span class="comment-user userinfo">Lucciniolo</span>
</div>
</div>
</div>
<div id="comment-tools-16967" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16967-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is answered" by SimonPoole 18 May '17, 23:31

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16989"></span>

<div id="answer-container-16989" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16989-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As you said, the extracts from bbbike.org have the version of all map objects set to -1. They also have all timestamps set to 1969. I'm not sure why, but this definitely makes them unusable for editing in JOSM.</p>
<p>I suppose you could modify the version manually by replacing <code>version="-1"</code> with <code>version="1"</code> in your downloaded extract before importing it. Or you could run some SQL queries on the database to change the version manually. You would need to update <code>version</code> in the tables: <code>current_nodes, current_ways and current_relations</code>. The <code>changeset_id</code> might need to be changed too but I'm not sure about that.</p>
<p>It might be easier to look for a different extract that provides the real OSM data with real version numbers instead of a modified version of it.</p>
<p>Other extract providers are listed on the wiki "<a href="https://wiki.openstreetmap.org/wiki/Planet">Planet</a>" page. I personally would recommend the geofabrik ones.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Oct '12, 05:19</strong></p>
<img src="https://secure.gravatar.com/avatar/43ae79d3345e19f30ea5f2ea64a9f7bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ToeBee&#39;s gravatar image" />
<p><span>ToeBee</span><br />
<span class="score" title="976 reputation points">976</span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ToeBee has 6 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-16989" class="comments-container">
<span id="56224"></span>
<div id="comment-56224" class="comment">
<div id="post-56224-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As explained by ToeBee, this is a problem with the OSM data you downloaded - the data contains wrong version values (namely -1). This is because <strong>the extracts from bbbike.org are not suitable for editing</strong>.</p>
<p>The FAQ at <a href="http://extract.bbbike.org/extract.html">http://extract.bbbike.org/extract.html</a> explains:</p>
<blockquote>
<p>The extracts don't contain metadata as version number, author, timestamp etc. If you need to edit OSM data, please go to the OpenStreetMap.org web site.</p>
</blockquote>
<p>Consequently, the extracts in Protocol Buffers format (.pbf) all have all version attributes set to -1, at least when I checked (2017-05-18).</p>
<p>The downloads in OSM XML format (.xml.gz) also do not contain a proper version, only there the version is always set to 1 instead of -1 (which is arguably even worse, because tools will not notice right away).</p>
<p>You will have to obtain OSM data from somewhere else.</p>
</div>
<div id="comment-56224-info" class="comment-info">
<span class="comment-age">(18 May '17, 09:55)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="56225"></span>
<div id="comment-56225" class="comment">
<div id="post-56225-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, manually "fixing" the version will not work (or cause even more trouble). JOSM needs the <em>right version</em> of each object to update it correctly. That information is simply missing in the downloads, there is no way to fix that.</p>
</div>
<div id="comment-56225-info" class="comment-info">
<span class="comment-age">(18 May '17, 09:56)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="56227"></span>
<div id="comment-56227" class="comment">
<div id="post-56227-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How would JOSM know whether the data contains the "right version" or not? There's no such thing. As long as JOSM gets a <em>valid</em> version number (ie. &gt;=1), it shouldn't have a problem opening it and working with it. Keep in mind that the database in question here is separate from the "live" OSM database and they didn't say anything about uploading this data to the OSM database, so mis-matching versions wouldn't be an issue.</p>
</div>
<div id="comment-56227-info" class="comment-info">
<span class="comment-age">(18 May '17, 16:34)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="56228"></span>
<div id="comment-56228" class="comment">
<div id="post-56228-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Folks this question was asked nearly 5 years ago, and is long outdated. not to mention that the author is unlikely to still be waiting for your input.</p>
</div>
<div id="comment-56228-info" class="comment-info">
<span class="comment-age">(18 May '17, 23:30)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-16989" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16989-form-container" class="comment-form-container">
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

