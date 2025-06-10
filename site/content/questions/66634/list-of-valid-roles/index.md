+++
type = "question"
title = "List of valid roles?"
description = '''When we check statistics of roles in all relations of a country (Planet dump), we see a big diversity of roles... And some of them not make sense. There are a list of valid roles? We can change by Overpass (mass edition) the invalid ones?  Example of Brazilian roles of (visible) relations that are m...'''
date = "2018-11-02T16:35:00Z"
lastmod = "2018-11-04T06:38:00Z"
weight = 66634
keywords = [ "quality", "quality_assurance", "roles", "relations", "metadata" ]
aliases = [ "/questions/66634" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [List of valid roles?](/questions/66634/list-of-valid-roles)

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
<span id="post-66634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66634-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When we check statistics of <a href="https://wiki.openstreetmap.org/wiki/Relation#Roles"><em>roles</em></a> in all <em>relations</em> of a country (Planet dump), we see a big diversity of <em>roles</em>... And some of them not make sense. <strong>There are a list of <em>valid roles</em>?</strong> We can change by Overpass (mass edition) the invalid ones?</p>
<hr />
<p>Example of Brazilian <em>roles</em> of (visible) <em>relations</em> that are <em>members of relations</em>:</p>
<pre><code> member_type |  n   
-------------|------
             | 2209
 subarea     |   96
 subbasin    |   56
 part        |   37
 route       |   33
 platform    |   22
 outer       |   11
 ...         | ...
 level_1     |    2
 riverbank   |    2
 stop        |    2
 land_area   |    1
 level_2     |    1
 main_stream |    1
 member      |    1
 perimeter   |    1</code></pre>
<p>Example of Brazilian <em>roles</em> of (visible) <em>ways</em> that are <em>members of relations</em>:</p>
<pre><code>           member_type           |   n    
---------------------------------+--------
 outer                           | 518757
                                 | 337283
 inner                           |  83125
 forward                         |  73637
 to                              |  50441
 from                            |  49544
 backward                        |   7231
 main_stream                     |   5210
 platform                        |   3259
 part                            |   2937
 outline                         |   1263
 via                             |    789
 link                            |    635
 ...                             |   ...
 Pokemon Go                      |      1
 Programa de Extensão            |      1
 Transporte público              |      1
 Volta                           |      1
 buildings                       |      1
 bus                             |      1
 conexão                         |      1
 edge                            |      1
 force                           |      1
 level_-?\d+                     |      1
 ouline                          |      1
 outlines                        |      1
 path                            |      1
 positive                        |      1
 ridge                           |      1
 shortcut                        |      1
 sim                             |      1
 stop:0                          |      1
 yes                             |      1</code></pre>
<p><strong>All are valid?</strong> "<code>level_1</code>", "<code>level_-?\d+</code>", "<a href="https://www.openstreetmap.org/api/0.6/relation/4049312"><code>level_2</code></a>", "<a href="https://www.openstreetmap.org/api/0.6/relation/8543189"><code>Pokemon Go</code></a>", accented values, etc.?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-quality" rel="tag" title="see questions tagged &#39;quality&#39;">quality</span> <span class="post-tag tag-link-quality_assurance" rel="tag" title="see questions tagged &#39;quality_assurance&#39;">quality_assurance</span> <span class="post-tag tag-link-roles" rel="tag" title="see questions tagged &#39;roles&#39;">roles</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-metadata" rel="tag" title="see questions tagged &#39;metadata&#39;">metadata</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Nov '18, 16:35</strong></p>
<img src="https://secure.gravatar.com/avatar/6963015ca2c3146e2a2a348b7fcb793b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppKrauss&#39;s gravatar image" />
<p><span>ppKrauss</span><br />
<span class="score" title="95 reputation points">95</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppKrauss has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Nov '18, 12:19</strong> </span></p>
</div>
</div>
<div id="comments-container-66634" class="comments-container">
<span id="66635"></span>
<div id="comment-66635" class="comment">
<div id="post-66635-score" class="comment-score">
1
</div>
<div class="comment-text">
<ol>
<li><p>What is "valid" for you?</p></li>
<li><p>Where do you want to "change by Overpass (mass edition)"? In the main, public OSM database or in your copy?</p></li>
</ol>
</div>
<div id="comment-66635-info" class="comment-info">
<span class="comment-age">(02 Nov '18, 18:51)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="66636"></span>
<div id="comment-66636" class="comment">
<div id="post-66636-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/5179/aseerel4c26"></a><a href="https://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a>, <strong>item 1</strong>: "valid" is not "so free", is something that make sense -- like <em>inner</em> and <em>outer</em> that are about topolody, an real information for map construction... I am looking for a standard/recommendation or good practice. Perhaps we can check a country like German and use it as reference model.</p>
</div>
<div id="comment-66636-info" class="comment-info">
<span class="comment-age">(03 Nov '18, 01:14)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
<span id="66637"></span>
<div id="comment-66637" class="comment">
<div id="post-66637-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>About item 2 (of <a href="https://help.openstreetmap.org/users/5179/aseerel4c26"></a><a href="https://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a>'s comment), let's wait the answer to make decisions... Cited Overpass only to show possible impact, when we suppose "full free".</p>
</div>
<div id="comment-66637-info" class="comment-info">
<span class="comment-age">(03 Nov '18, 01:17)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
</div>
<div id="comment-tools-66634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66634-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="66638"></span>

<div id="answer-container-66638" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66638-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ppKrauss has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can look at the OpenStreetMap wiki to find out documented <a href="https://wiki.openstreetmap.org/wiki/Map_Features">features</a>, and see some common <a href="https://wiki.openstreetmap.org/wiki/Relation">relations</a>. Also <a href="https://taginfo.openstreetmap.org/relations">TagInfo</a> can help you to see which relations and tag combinations are common.</p>
<p>As for the other less-known or undocumented tags to describe, they are just that. They are not necessarily wrong. Although sometimes there might be typo, the others were added because the mapper(s) though that was the best way to describe the feature. There is no reason to remove or alter them on a large scale. You could ask each mapper to document them, or discuss with them whether there is a documented way to express the same, etc. But you will probably find this too time consuming.</p>
<p>So my advice is, to just ignore the values you are not intested in.</p>
<p>Marc Zoutendijk wrote a series of <a href="https://www.openstreetmap.org/user/marczoutendijk/diary">diary posts</a> called "Improving the OSM map - why don’t we" on exactly those 1 off tags you find everywhere. Don't forget to read the comments, to find out other mappers ideas about this "problem".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Nov '18, 06:46</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-66638" class="comments-container">
<span id="66639"></span>
<div id="comment-66639" class="comment">
<div id="post-66639-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/5390/escada">@escada</a>, thanks all explanations! Is important to see, from experient mapper as you, an assertion <em>"just ignore the values you are not interested in"</em>: confirming the "full free/no control" hypothesis for relation-roles... But what Wiki say as "free format text field" is not the same as "free semantic". So, you also showed the spirit of the thing (good links!).</p>
</div>
<div id="comment-66639-info" class="comment-info">
<span class="comment-age">(03 Nov '18, 08:23)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
<span id="66640"></span>
<div id="comment-66640" class="comment">
<div id="post-66640-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My only residual doubt is about <strong>specialized documentation</strong> (for role-values not for usual tag-values), can I start/complement something <a href="https://wiki.openstreetmap.org/wiki/Relation#Roles">at Relation#Roles Wiki</a> using your answer? There are something (you see?) with specialized comments about relation-role-values, that I can cite there? ... Or something about <em>consistency</em> between role-values and the tags of the pointed element?</p>
</div>
<div id="comment-66640-info" class="comment-info">
<span class="comment-age">(03 Nov '18, 08:24)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
<span id="66643"></span>
<div id="comment-66643" class="comment">
<div id="post-66643-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... Perhaps the main documentation is to consolidate in one place a summary of all reccomendations: a typical exception to the rule of thumb (full free/no control) is the explicit <a href="https://wiki.openstreetmap.org/wiki/Tag:waterway%3Driverbank#Islands">instruction for islands</a>.</p>
</div>
<div id="comment-66643-info" class="comment-info">
<span class="comment-age">(03 Nov '18, 12:39)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
<span id="66649"></span>
<div id="comment-66649" class="comment">
<div id="post-66649-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Everybody is free to write wiki pages. Those pages (if not in your private space), are a community effort. So others might change and or discuss the content of what you write.</p>
</div>
<div id="comment-66649-info" class="comment-info">
<span class="comment-age">(04 Nov '18, 06:38)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-66638" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66638-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66641"></span>

<div id="answer-container-66641" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66641-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>For Portuguese readers...</strong></p>
<p>A principal fonte de documentação parece ser a estatística de uso, e isso inclui a correlação entre a tag <em>type</em> do elemento apontado e a <em>role</em> utilizada, conforme destacado na ilustração abaixo ("sem papel" indica uso frequente de <em>role</em> vazia).</p>
<p><img src="https://help.openstreetmap.org/upfiles/relation-role-main01.720px.png" alt="alt text" /></p>
<p>Fonte: <a href="https://taginfo.openstreetmap.org/relations">taginfo.openstreetmap.org/relations</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Nov '18, 09:14</strong></p>
<img src="https://secure.gravatar.com/avatar/6963015ca2c3146e2a2a348b7fcb793b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppKrauss&#39;s gravatar image" />
<p><span>ppKrauss</span><br />
<span class="score" title="95 reputation points">95</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppKrauss has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-66641" class="comments-container">
&#10;</div>
<div id="comment-tools-66641" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66641-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

