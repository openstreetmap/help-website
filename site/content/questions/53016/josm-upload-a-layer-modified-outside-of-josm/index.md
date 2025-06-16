+++
type = "question"
title = "JOSM Upload a layer modified outside of JOSM"
description = '''I have used this Overpass query to download all the highways of a given city (indicated by XXXXXX) that have the tag name. The data was saved into a file. &amp;lt;osm-script output=&quot;xml&quot;&amp;gt;  &amp;lt;id-query {{nominatimArea:XXXXXX}} into=&quot;area&quot;/&amp;gt;  &amp;lt;query type=&quot;way&quot;&amp;gt;  &amp;lt;has-kv k=&quot;highway&quot;/&amp;gt;  &amp;...'''
date = "2016-11-17T22:18:00Z"
lastmod = "2016-11-19T20:57:00Z"
weight = 53016
keywords = [ "josm", "layer", "upload", "file" ]
aliases = [ "/questions/53016" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM Upload a layer modified outside of JOSM](/questions/53016/josm-upload-a-layer-modified-outside-of-josm)

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
<span id="post-53016-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53016-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53016-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have used this Overpass query to download all the <em>highways</em> of a given city (indicated by XXXXXX) that have the tag <em>name</em>. The data was saved into a file.</p>
<pre><code>&lt;osm-script output=&quot;xml&quot;&gt;
  &lt;id-query {{nominatimArea:XXXXXX}} into=&quot;area&quot;/&gt;
  &lt;query type=&quot;way&quot;&gt;
    &lt;has-kv k=&quot;highway&quot;/&gt;
    &lt;has-kv k=&quot;name&quot;/&gt;
    &lt;area-query from=&quot;area&quot;/&gt;
  &lt;/query&gt;
  &lt;union&gt;
    &lt;item /&gt;
      &lt;recurse type=&quot;way-node&quot;/&gt;   
  &lt;/union&gt;
  &lt;print mode=&quot;meta&quot; /&gt;
&lt;/osm-script&gt;</code></pre>
<p>Outside of JOSM, with a very smart script, I've parsed the OSM file to check if the highway's names were correct: if not, the script change them to the correct values. Keep in mind that I know exactly which way (hence its ID) is going to be modified. When the edit is done, I would like to upload the file to OSM through JOSM: if I click the Upload button, JOSM tells me "No changes to upload".</p>
<p>So far I thought about two possibilities:</p>
<ol>
<li>Download the area of the edit, then load my layer, and finally merge them. Then upload. Though, this is not feasible for me because I'm working on entire cities: the data to download would be too large.</li>
<li>Obviously JOSM is able to detect the changes to a layer. Is there any tag I can add to the modified ways in order to get JOSM to upload them?</li>
</ol>
<p>If you have any other suggestions, please keep them coming. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Nov '16, 22:18</strong></p>
<img src="https://secure.gravatar.com/avatar/b88a31e4097701d418799b31e1892771?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Davide_sd&#39;s gravatar image" />
<p><span>Davide_sd</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Davide_sd has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53016" class="comments-container">
<span id="53019"></span>
<div id="comment-53019" class="comment">
<div id="post-53019-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Side note: please follow the <a href="https://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct">Automated Edits code of conduct</a> and keep in mind that you cannot use every source as reference due to copyright/database laws.</p>
</div>
<div id="comment-53019-info" class="comment-info">
<span class="comment-age">(17 Nov '16, 22:44)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="53038"></span>
<div id="comment-53038" class="comment">
<div id="post-53038-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><del>Side note2: I <em>guess</em> this may be an edit which is the result: <a href="https://www.openstreetmap.org/changeset/43802055">https://www.openstreetmap.org/changeset/43802055</a> (4 ways, 6 nodes edited).</del></p>
</div>
<div id="comment-53038-info" class="comment-info">
<span class="comment-age">(19 Nov '16, 19:13)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="53039"></span>
<div id="comment-53039" class="comment">
<div id="post-53039-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>No! This is the changeset: <a href="https://www.openstreetmap.org/changeset/43777145">https://www.openstreetmap.org/changeset/43777145</a></p>
</div>
<div id="comment-53039-info" class="comment-info">
<span class="comment-age">(19 Nov '16, 20:24)</span> <span class="comment-user userinfo">Davide_sd</span>
</div>
</div>
<span id="53041"></span>
<div id="comment-53041" class="comment">
<div id="post-53041-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ah, thanks for the link, Davide_sd! :-) (the wiki page in the description tag is helpful … I just need to learn more Italian)</p>
</div>
<div id="comment-53041-info" class="comment-info">
<span class="comment-age">(19 Nov '16, 20:57)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53016" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53016-form-container" class="comment-form-container">
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

<span id="53020"></span>

<div id="answer-container-53020" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53020-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-53020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Davide_sd has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>JOSM adds a <code>action='modify'</code> attribute to modified objects. Just try it: do a change in JOSM and save the file to .osm and have a look. See also <a href="https://wiki.openstreetmap.org/wiki/JOSM_file_format">https://wiki.openstreetmap.org/wiki/JOSM_file_format</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Nov '16, 22:45</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Nov '16, 22:50</strong> </span></p>
</div>
</div>
<div id="comments-container-53020" class="comments-container">
<span id="53022"></span>
<div id="comment-53022" class="comment">
<div id="post-53022-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You are the man! Thank you!!! :) And yes, I'll be extremely careful with the script!</p>
</div>
<div id="comment-53022-info" class="comment-info">
<span class="comment-age">(17 Nov '16, 22:50)</span> <span class="comment-user userinfo">Davide_sd</span>
</div>
</div>
<span id="53026"></span>
<div id="comment-53026" class="comment">
<div id="post-53026-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>can you show the code of your script somewhere, so others can have a look at it ?</p>
</div>
<div id="comment-53026-info" class="comment-info">
<span class="comment-age">(18 Nov '16, 04:20)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="53040"></span>
<div id="comment-53040" class="comment">
<div id="post-53040-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I will, but first I have to fix some bugs...</p>
</div>
<div id="comment-53040-info" class="comment-info">
<span class="comment-age">(19 Nov '16, 20:26)</span> <span class="comment-user userinfo">Davide_sd</span>
</div>
</div>
</div>
<div id="comment-tools-53020" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53020-form-container" class="comment-form-container">
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

