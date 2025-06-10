+++
type = "question"
title = "Getting way ids from raw osm file"
description = '''The are a few tools, which ingest OSM ways ids, but there is no tool to get them from a &quot;.osm&quot; file. Is there any tool (pyosmium?) to print all ways ids from a osm file containing ways, nodes and relations?'''
date = "2018-03-09T08:55:00Z"
lastmod = "2018-03-12T14:49:00Z"
weight = 62597
keywords = [ "linux", "grep", ".osm", "id" ]
aliases = [ "/questions/62597" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting way ids from raw osm file](/questions/62597/getting-way-ids-from-raw-osm-file)

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
<span id="post-62597-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62597-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62597-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The are a few tools, which ingest OSM ways ids, but there is no tool to get them from a ".osm" file.</p>
<p>Is there any tool (pyosmium?) to print all ways ids from a osm file containing ways, nodes and relations?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span> <span class="post-tag tag-link-grep" rel="tag" title="see questions tagged &#39;grep&#39;">grep</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Mar '18, 08:55</strong></p>
<img src="https://secure.gravatar.com/avatar/8e0867aa963fc989a200f2f35144d3c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="landuse&#39;s gravatar image" />
<p><span>landuse</span><br />
<span class="score" title="116 reputation points">116</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="landuse has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Mar '18, 21:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-62597" class="comments-container">
<span id="62598"></span>
<div id="comment-62598" class="comment">
<div id="post-62598-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A command-line tool such as "grep" will get you a list - is that what you want? What OS are you running?</p>
</div>
<div id="comment-62598-info" class="comment-info">
<span class="comment-age">(09 Mar '18, 09:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="62599"></span>
<div id="comment-62599" class="comment">
<div id="post-62599-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Linux of course</p>
</div>
<div id="comment-62599-info" class="comment-info">
<span class="comment-age">(09 Mar '18, 09:30)</span> <span class="comment-user userinfo">landuse</span>
</div>
</div>
<span id="62603"></span>
<div id="comment-62603" class="comment">
<div id="post-62603-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>grep "&lt;way" my-osm-file.osm | cut -d\" -f2</p>
</div>
<div id="comment-62603-info" class="comment-info">
<span class="comment-age">(09 Mar '18, 10:13)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="62605"></span>
<div id="comment-62605" class="comment">
<div id="post-62605-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Processing XML with the usual unix text processing tools always feels like doing things wrong, but then again, I'm not aware of a tool that does it better in a "pure XML" way. Is there one? There ought to be some sort of grep-like tool that takes XPath expressions...</p>
</div>
<div id="comment-62605-info" class="comment-info">
<span class="comment-age">(09 Mar '18, 16:54)</span> <span class="comment-user userinfo">turepalsson</span>
</div>
</div>
<span id="62606"></span>
<div id="comment-62606" class="comment">
<div id="post-62606-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The problem with actually trying to parse the XML is that you potentially have to load a very large amount of data to do so. There are XML processors around, but trying to do it that way will be much slower and more complicated that the way described above.</p>
<p>If on the other hand you wanted a list of "ways with a certain tag", then the answer might be different.</p>
</div>
<div id="comment-62606-info" class="comment-info">
<span class="comment-age">(09 Mar '18, 16:58)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62597" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62597-form-container" class="comment-form-container">
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

<span id="62644"></span>

<div id="answer-container-62644" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62644-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62644-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62644-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the file is not too big you can use <em>xmlstarlet</em>:</p>
<pre><code>xmlstarlet sel -t -m /osm/way -v @id -n /path/file</code></pre>
<p>The problem with this program is that it uses lots of RAM and with the usual OpenStreetMap osm files it easily fills up the RAM of an average desktop PC without even producing any output.</p>
<p>Otherwise there is <em>osmium</em>, a command tool which can print IDs on the standard output; then you have to filter what you need with awk/sed:</p>
<pre><code>osmium cat -f opl /path/file | awk &#39;/^w/{print substr($1,2)}&#39;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '18, 14:49</strong></p>
<img src="https://secure.gravatar.com/avatar/9c8957ccf79025bf749665ebec2bdfa2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MarcoR&#39;s gravatar image" />
<p><span>MarcoR</span><br />
<span class="score" title="687 reputation points">687</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MarcoR has 5 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-62644" class="comments-container">
&#10;</div>
<div id="comment-tools-62644" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62644-form-container" class="comment-form-container">
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

