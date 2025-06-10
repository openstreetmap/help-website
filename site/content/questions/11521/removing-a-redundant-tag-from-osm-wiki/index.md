+++
type = "question"
title = "Removing a redundant tag from OSM wiki"
description = '''OSM wiki contains a tag landuse=peat_cutting. This tag can already be expressed through landuse=quarry, resource=peat. What is the process of removing such tag from the wiki?'''
date = "2012-03-27T13:34:00Z"
lastmod = "2012-03-28T13:11:00Z"
weight = 11521
keywords = [ "wiki", "tags" ]
aliases = [ "/questions/11521" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Removing a redundant tag from OSM wiki](/questions/11521/removing-a-redundant-tag-from-osm-wiki)

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
<span id="post-11521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11521-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>OSM wiki contains a tag landuse=peat_cutting. This tag can already be expressed through landuse=quarry, resource=peat.</p>
<p>What is the process of removing such tag from the wiki?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wiki" rel="tag" title="see questions tagged &#39;wiki&#39;">wiki</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Mar '12, 13:34</strong></p>
<img src="https://secure.gravatar.com/avatar/3cedb07ada6a9c89c1f2de5fbebcbcf4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="extropy&#39;s gravatar image" />
<p><span>extropy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="extropy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11521" class="comments-container">
&#10;</div>
<div id="comment-tools-11521" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11521-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="11523"></span>

<div id="answer-container-11523" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11523-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-11523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tag <code>landuse=peat_cutting</code> is used over 250 times in OSM, whereas <code>landuse=quarry,resource=peat</code> is used zero times. (In addition, there are about 70 instances of <code>landuse=quarry,quarry:type=peat_cutting</code>.) It would therefore be wrong and misleading to remove documentation about <code>landuse=peat_cutting</code> from the wiki.</p>
<p>Remember that the Wiki is not there to document what "could" be or what someone thinks would be the cleanest, safest, nicest way to tag something - the Wiki is there to document what is actually used.</p>
<p>Edit: Pieren has pointed out that my numbers above are wrong. Indeed, <code>resource=peat</code> does have over 400 uses. This does not however change the fact that <code>landuse=peat_cutting</code> should not be simply deleted.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '12, 13:39</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Mar '12, 13:22</strong> </span></p>
</div>
</div>
<div id="comments-container-11523" class="comments-container">
<span id="11524"></span>
<div id="comment-11524" class="comment">
<div id="post-11524-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Also, classifying peat cutting as a type of quarry sounds awful to me. Peat is growing, living matter. Quarries dig out mineral, non-living rocks. Would you classify, say, timber or potatoes as a type of quarry too ? I know words (particularly English ones) change meaning between continents, but that alledged meaning of "quarry" is just too odd.</p>
</div>
<div id="comment-11524-info" class="comment-info">
<span class="comment-age">(27 Mar '12, 14:05)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-11523" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11523-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11525"></span>

<div id="answer-container-11525" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11525-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Frederik already gave a good answer for that particular tagging scheme, but to answer the more general question:</p>
<p>Changing something in the wiki starts by gathering consensus. Consensus can be obtained by :</p>
<ul>
<li>Seeing that the tagging scheme is already widely used in the database (<a href="http://taginfo.openstreetmap.org/">taginfo</a> should be the first thing you check).</li>
<li>Discussing things in the relevant wiki page's discussion tab, in the (tagging) <a href="http://wiki.openstreetmap.org/wiki/MailingLists">mailing list</a>, or on IRC</li>
<li>Writing a <a href="http://wiki.openstreetmap.org/wiki/Proposal">proposal</a> and getting it aproved</li>
<li>Seeing it supported by various tools, especially the renderers and editors</li>
</ul>
<p>Once the consensus is clear and the tagging scheme is being used in the wild, you can go ahead and edit the wiki.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '12, 14:21</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-11525" class="comments-container">
&#10;</div>
<div id="comment-tools-11525" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11525-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11553"></span>

<div id="answer-container-11553" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11553-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>On taginfo, we find <a href="http://taginfo.openstreetmap.org/tags/resource=peat#overview">478 resource=peat</a> (and one "resource=Peat")<br />
On those, <a href="http://overpass-api.de/api/xapi_meta?*%5Bresource%3Dpeat%5D%5Blanduse%3Dquarry%5D">477 are combined with "landuse=quarry"</a></p>
<p>The database is not consistent. But it is not a reason to have the same inconsistency on the wiki. You should initiate a discussion on the <a href="http://wiki.openstreetmap.org/wiki/Mailing_list">tagging mailing list</a>. The result should be a consensus for one of the versions present in the database and the wiki enhanced with that consensus (explaining the different existing values and combinations but we recommand only one).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '12, 13:11</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Mar '12, 14:15</strong> </span></p>
</div>
</div>
<div id="comments-container-11553" class="comments-container">
&#10;</div>
<div id="comment-tools-11553" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11553-form-container" class="comment-form-container">
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

