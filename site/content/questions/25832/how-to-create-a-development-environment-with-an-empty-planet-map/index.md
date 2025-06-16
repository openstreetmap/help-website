+++
type = "question"
title = "How to create a development environment with an empty planet map?"
description = '''The format of OSM is great for me! But i need have a planet no data. After would do importing the database specific. it&#x27;s possible? How to do? My OSM source is ruby on rails and my server start with data. I followed this tutorial: https://wiki.openstreetmap.org/wiki/Rails#Installing_Rails'''
date = "2013-08-26T22:23:00Z"
lastmod = "2013-08-27T22:56:00Z"
weight = 25832
keywords = [ "development", "import", "database" ]
aliases = [ "/questions/25832" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to create a development environment with an empty planet map?](/questions/25832/how-to-create-a-development-environment-with-an-empty-planet-map)

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
<span id="post-25832-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25832-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-25832-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The format of OSM is great for me! But i need have a planet no data. After would do importing the database specific. it's possible?</p>
<p>How to do?</p>
<p>My OSM source is ruby on rails and my server start with data. I followed this tutorial: <a href="https://wiki.openstreetmap.org/wiki/Rails#Installing_Rails">https://wiki.openstreetmap.org/wiki/Rails#Installing_Rails</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Aug '13, 22:23</strong></p>
<img src="https://secure.gravatar.com/avatar/f84a11d51987ce5e97fc36474fde8329?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leonardo%20Neves&#39;s gravatar image" />
<p><span>Leonardo Neves</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leonardo Neves has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Aug '13, 11:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0c12497903c6f3b2dd9f4d87deb127de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MagicFab&#39;s gravatar image" />
<p><span>MagicFab</span><br />
<span class="score" title="935 reputation points">935</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span></p>
</div>
</div>
<div id="comments-container-25832" class="comments-container">
&#10;</div>
<div id="comment-tools-25832" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25832-form-container" class="comment-form-container">
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

<span id="25844"></span>

<div id="answer-container-25844" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25844-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-25844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This question came up on IRC a little while ago. I can't find it in my logs, or who should get the credit, but the answer was to do everything as normal except use an empty-but-valid osm-xml file during the data import. The file should be something like:</p>
<pre><code> &lt; ?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
 &lt; osm version=&quot;0.6&quot; generator=&quot;CGImap 0.0.2&quot;&gt;
 &lt; bounds minlat=&quot;54.0889580&quot; minlon=&quot;12.2487570&quot; maxlat=&quot;54.0913900&quot; maxlon=&quot;12.2524800&quot;/&gt;
 &lt; /osm&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '13, 10:29</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-25844" class="comments-container">
<span id="25869"></span>
<div id="comment-25869" class="comment">
<div id="post-25869-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Vincent, the empty osm not work =/ The data carry on being downloadeds. Thanks for answer!</p>
<p>What i seek is build a local map only with local OSM file. No internet connection.</p>
<p>thanks all for helping! I gonna carry on, if i have success post here.</p>
</div>
<div id="comment-25869-info" class="comment-info">
<span class="comment-age">(27 Aug '13, 20:03)</span> <span class="comment-user userinfo">Leonardo Neves</span>
</div>
</div>
</div>
<div id="comment-tools-25844" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25844-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="25836"></span>

<div id="answer-container-25836" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25836-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This sounds like an uncommon request and since it is development related, the knowledgeable people are found in the dev <a href="https://wiki.openstreetmap.org/wiki/Mailing_lists">mailing list</a>.</p>
<p>I would expect that you should skip the <a href="https://wiki.openstreetmap.org/wiki/Rails#Populating_the_database">Populating the Database</a> section. The following comment would suggest adding data should be done through change sets.</p>
<blockquote>
<p>Later updates to the database (sometimes referred to as the apidb) will need to use a change format (.osc).</p>
</blockquote>
<p>If you have success, I suggest you write docs on how to use an empty database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '13, 02:53</strong></p>
<img src="https://secure.gravatar.com/avatar/7e77c05737bf455a5bf99c0f17ac19d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="he_the_great&#39;s gravatar image" />
<p><span>he_the_great</span><br />
<span class="score" title="1175 reputation points"><span>1.2k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="he_the_great has 3 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-25836" class="comments-container">
<span id="25879"></span>
<div id="comment-25879" class="comment">
<div id="post-25879-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not 100% sure that I understand the question, but isn't it just a case of running "osmosis" (in the Populating the Database section) with an empty or nearly-empty-but-valid ** XML file instead of the planet one?</p>
<p>Perhaps you could explain in a little more detail what you're trying to do and what problems you're still seeing?</p>
<p>** I don't know, but suspect that running osmosis might do some schema setup in addition to the data loading, and giving it "something" to load might be required.</p>
</div>
<div id="comment-25879-info" class="comment-info">
<span class="comment-age">(27 Aug '13, 22:56)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-25836" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25836-form-container" class="comment-form-container">
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

