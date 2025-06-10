+++
type = "question"
title = "nominatim setup with local tiles"
description = '''Hi,  From Google, I understand that to create an interface same as https://www.openstreetmap.org, where User can search for location, I will need to use nominatim.  I am reading bellow link, http://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-16/ I understand i will need to install a...'''
date = "2018-05-25T12:32:00Z"
lastmod = "2018-05-28T01:42:00Z"
weight = 63733
keywords = [ "nominatim" ]
aliases = [ "/questions/63733" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nominatim setup with local tiles](/questions/63733/nominatim-setup-with-local-tiles)

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
<span id="post-63733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63733-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, From Google, I understand that to create an interface same as <a href="https://www.openstreetmap.org">https://www.openstreetmap.org</a>, where User can search for location, I will need to use nominatim. I am reading bellow link, <a href="http://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-16/">http://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-16/</a></p>
<p>I understand i will need to install a new server, but what I dont understand is, how will create relation between my existing tiles server 192.168.1.32/hot and this new nominatim server ? how nomatiam will know from where to find tiles infomration ( /var/lib/mod_tile/ajt/ in 192.168.1.32 )</p>
<p>also,</p>
<p>Here, i am just working with one country. I guess i can build nominatim in the same server where i have the files, but still i have the same qustion , how will nominatim know from where to get teh tiles information ? is this from this section , what Path its looking for ? the tiles path ?</p>
<pre><code>@define(&#39;CONST_Osm2pgsql_Flatnode_File&#39;, &#39;/path/to/flatnode.file&#39;);</code></pre>
<p>My tiles configurtion:</p>
<pre><code>Localserver for tiles : 192.168.1.32
web access : 192.168.1.32/hot
file system location : /var/lib/mod_tile/ajt/</code></pre>
<p>Thanks for the help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '18, 12:32</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb2a94f867841b58214be09992831d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fosiul&#39;s gravatar image" />
<p><span>fosiul</span><br />
<span class="score" title="96 reputation points">96</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fosiul has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 May '18, 12:58</strong> </span></p>
</div>
</div>
<div id="comments-container-63733" class="comments-container">
<span id="63759"></span>
<div id="comment-63759" class="comment">
<div id="post-63759-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello All, Here I just want to know how Nominatim wil know from where to serve the tiles ? Any help will be really appreciated</p>
<p>Thanks</p>
</div>
<div id="comment-63759-info" class="comment-info">
<span class="comment-age">(27 May '18, 11:51)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
</div>
<div id="comment-tools-63733" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63733-form-container" class="comment-form-container">
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

<span id="63769"></span>

<div id="answer-container-63769" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63769-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim and tiles are separate technologies/projects. You can install them on the same server, but Nominatim will build its own database (called 'nominatim') and not share any data with your tile service. Nominatim has its own update scripts for the database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 May '18, 00:23</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-63769" class="comments-container">
<span id="63771"></span>
<div id="comment-63771" class="comment">
<div id="post-63771-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Got it , I thought Nominatim and RAis port are some how same. Thanks for the confermation.</p>
</div>
<div id="comment-63771-info" class="comment-info">
<span class="comment-age">(28 May '18, 01:42)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
</div>
<div id="comment-tools-63769" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63769-form-container" class="comment-form-container">
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

