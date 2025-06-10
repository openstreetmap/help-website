+++
type = "question"
title = "Not add extra attributes when import  .pbf file to database"
description = '''I&#x27;m using osm2pgsql I&#x27;m importing a file called maryland.osm.pbf with extra atributes (--extra-attributes )  but   osm_uid  osm_user fields  osm_version   osm_timestamp are empty.i don&#x27;t know why?  osm2pgsql --extra-attributes -v -S default.style -d db_maryland maryland.osm.pbf    while, if I import...'''
date = "2013-02-07T00:03:00Z"
lastmod = "2014-11-06T11:07:00Z"
weight = 19647
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/19647" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Not add extra attributes when import .pbf file to database](/questions/19647/not-add-extra-attributes-when-import-pbf-file-to-database)

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
<span id="post-19647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19647-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-19647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using osm2pgsql</p>
<p>I'm importing a file called maryland.osm.pbf with extra atributes (--extra-attributes ) but</p>
<ul>
<li>osm_uid</li>
<li>osm_user fields<br />
</li>
<li>osm_version</li>
<li><p>osm_timestamp are empty.i don't know why?</p>
<pre><code>osm2pgsql --extra-attributes -v  -S default.style -d db_maryland  maryland.osm.pbf</code></pre></li>
</ul>
<p>while, if I import a file maryland.osm.bz2. is normal.Extra attributes appear</p>
<pre><code>osm2pgsql --extra-attributes -v  -S default.style -d db_maryland  maryland.osm.bz2.</code></pre>
<p>I need to import. PBF files. please help me.</p>
<p>in my file default.style is enabled the fields for extra atributes.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Feb '13, 00:03</strong></p>
<img src="https://secure.gravatar.com/avatar/407d8e57e3058ea1969d515f44547556?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rub21&#39;s gravatar image" />
<p><span>Rub21</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rub21 has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-19647" class="comments-container">
<span id="38347"></span>
<div id="comment-38347" class="comment">
<div id="post-38347-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am also seeing this problem. There's a bug report <a href="https://github.com/openstreetmap/osm2pgsql/issues/137">https://github.com/openstreetmap/osm2pgsql/issues/137</a></p>
</div>
<div id="comment-38347-info" class="comment-info">
<span class="comment-age">(06 Nov '14, 10:36)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
<span id="38348"></span>
<div id="comment-38348" class="comment">
<div id="post-38348-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to confirm, the PBF that you're using really does include the extra attributes in the first place, does it?</p>
<p>FWIW I believe that Geofabrik PBFs do include at least the user's display name because when I process PBFs (not using osm2pgsql) I do processing based on that which works.</p>
</div>
<div id="comment-38348-info" class="comment-info">
<span class="comment-age">(06 Nov '14, 11:07)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-19647" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19647-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

