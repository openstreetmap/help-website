+++
type = "question"
title = "search for objects created by a specific author in JOSM"
description = '''There is a user which is mapping many buildings and putting random building heights and levels on them. He is mapping them oblique angled, even if they are clearly visible as right angled on areal photographs (and in reality, of course). Even flat pitches and open-air theaters and so on are mapped a...'''
date = "2014-01-08T08:52:00Z"
lastmod = "2014-01-08T14:59:00Z"
weight = 29655
keywords = [ "josm", "search", "objects", "author" ]
aliases = [ "/questions/29655" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [search for objects created by a specific author in JOSM](/questions/29655/search-for-objects-created-by-a-specific-author-in-josm)

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
<span id="post-29655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29655-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-29655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There is a user which is mapping many buildings and putting random building heights and levels on them. He is mapping them oblique angled, even if they are clearly visible as right angled on areal photographs (and in reality, of course). Even flat pitches and open-air theaters and so on are mapped as buildings.</p>
<p>He is mapping all over the world. And I don’t want to correct everything. But in my region, where I know where the buildings are and can correct the height, I want to find everything he mapped. Now my question:</p>
<p><strong>How can I search for objects an author created in JOSM?</strong> I have tried the JOSM search function with <code>author:68arti</code> but that didn’t find anything. What is the correct syntax?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-objects" rel="tag" title="see questions tagged &#39;objects&#39;">objects</span> <span class="post-tag tag-link-author" rel="tag" title="see questions tagged &#39;author&#39;">author</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jan '14, 08:52</strong></p>
<img src="https://secure.gravatar.com/avatar/793c9f0cfb9f3cc6001d73f127644c67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erik&#39;s gravatar image" />
<p><span>erik</span><br />
<span class="score" title="558 reputation points">558</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erik has one accepted answer">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jan '14, 11:01</strong> </span></p>
</div>
</div>
<div id="comments-container-29655" class="comments-container">
&#10;</div>
<div id="comment-tools-29655" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29655-form-container" class="comment-form-container">
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

<span id="29667"></span>

<div id="answer-container-29667" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29667-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29667-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-29667-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="erik has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a few ways you can do this :</p>
<p>In josm, use a search string such as</p>
<pre><code>user:&quot;Vincent de Phily&quot;</code></pre>
<p>To avoid having to download data beforehand, you can use the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">overpass API</a> with this <a href="http://overpass-turbo.eu/">web GUI</a>. Use a query like</p>
<p>&lt;query type="node"&gt;&lt;user name="Vincent de Phily"/&gt;&lt;bbox-query {{bbox}}/&gt;&lt;/query&gt;&lt;print mode="meta"/&gt;</p>
<p>Those two methods have the drawback that they'll only find objects if the user in question is the last modifier of the object. That's probably what you want in this case (to avoid finding objects again once you've modified them), but you need to keep that restriction in mind.</p>
<p>Another tool you can use is the <a href="http://yosmhm.neis-one.org/">user heatmap</a>, and maybe <a href="http://hdyc.neis-one.org/">how did you contribute</a>. Both will give you usefull info about a particular mapper.</p>
<p>Lastly, as Andy already mentioned, you really should try to contact the mapper instead of starting an edit war. Educating contributors can sometimes be complicated / frustrating (most of the time it's simple and rewarding :p ) but it is better for everybody in the long run.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '14, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-29667" class="comments-container">
<span id="29686"></span>
<div id="comment-29686" class="comment">
<div id="post-29686-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Very nice answer. Good idea to use the overpass API instead of loading all data of the specific region into JOSM. But as the user added just buildings, the correct overpass request would look</p>
<pre><code>&lt;query type=&quot;way&quot;&gt;&lt;user name=&quot;68arti&quot;/&gt;&lt;bbox-query {{bbox}}/&gt;&lt;/query&gt;
&lt;union&gt;
  &lt;item/&gt;
  &lt;recurse type=&quot;down&quot;/&gt;
&lt;/union&gt;
&lt;print mode=&quot;meta&quot;/&gt;</code></pre>
<p>run it, and then click on export and open it with JOSM. Thank you.</p>
</div>
<div id="comment-29686-info" class="comment-info">
<span class="comment-age">(08 Jan '14, 14:59)</span> <span class="comment-user userinfo">erik</span>
</div>
</div>
</div>
<div id="comment-tools-29667" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29667-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29657"></span>

<div id="answer-container-29657" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29657-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is probably best to send him a nice diplomatic message. see this question <a href="/questions/1850/how-do-a-i-contact-a-moderator-about-a-mailing-list-message">https://help.openstreetmap.org/questions/1850/how-do-a-i-contact-a-moderator-about-a-mailing-list-message</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '14, 09:08</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jan '14, 09:10</strong> </span></p>
</div>
</div>
<div id="comments-container-29657" class="comments-container">
<span id="29660"></span>
<div id="comment-29660" class="comment">
<div id="post-29660-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, but this does not answer my question. And of course I have send a message to the author, but I only got a rude answer, that he/she doesn’t bother and I should do it better. He is continuing to contribute buildings, where no buildings are. Oblique angled and with random height. But please, answer my question.</p>
</div>
<div id="comment-29660-info" class="comment-info">
<span class="comment-age">(08 Jan '14, 09:48)</span> <span class="comment-user userinfo">erik</span>
</div>
</div>
</div>
<div id="comment-tools-29657" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29657-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29670"></span>

<div id="answer-container-29670" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29670-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29670-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29670-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The solution to search in JOSM for all objects that user 68arti created (and were never touched afterwards) is:</p>
<pre><code>user:68arti version:1</code></pre>
<p>In pictures:</p>
<p>Select the "show authors" dialogue: <img src="http://i.imgur.com/RVJrb4J.jpg" /></p>
<p>Open the search (you can use the keyboard shortcut ctrl+f: <img src="http://i.imgur.com/9GDtESQ.jpg" /></p>
<p>Enter the search item (in this case I search for a user): <img src="http://i.imgur.com/hKptOgI.jpg" /></p>
<p>View the results: <img src="http://i.imgur.com/ReSdmw4.jpg" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '14, 10:59</strong></p>
<img src="https://secure.gravatar.com/avatar/793c9f0cfb9f3cc6001d73f127644c67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erik&#39;s gravatar image" />
<p><span>erik</span><br />
<span class="score" title="558 reputation points">558</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erik has one accepted answer">9%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jan '14, 16:48</strong> </span></p>
</div>
</div>
<div id="comments-container-29670" class="comments-container">
<span id="29679"></span>
<div id="comment-29679" class="comment">
<div id="post-29679-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>That doesn't work the way you think. It'll only return objects that currently are at version 1. So if 68arti created a way and anybody (you or 68arti) edited it, it won't show up in your query.</p>
<p>I think that josm only holds the latest version in memory, so that its search function cannot look at old versions of an object.</p>
</div>
<div id="comment-29679-info" class="comment-info">
<span class="comment-age">(08 Jan '14, 13:22)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="29681"></span>
<div id="comment-29681" class="comment">
<div id="post-29681-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>True. Otherwise it would have to fetch the full history for every element which is a rather heavy operation.</p>
</div>
<div id="comment-29681-info" class="comment-info">
<span class="comment-age">(08 Jan '14, 13:58)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="29683"></span>
<div id="comment-29683" class="comment">
<div id="post-29683-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Maybe JOSM is not loading all versions. But if you search for version 1 then you only get objects, which have never been edited by anybody else. And that is what I wanted to do. I will edit my answer.</p>
</div>
<div id="comment-29683-info" class="comment-info">
<span class="comment-age">(08 Jan '14, 14:28)</span> <span class="comment-user userinfo">erik</span>
</div>
</div>
</div>
<div id="comment-tools-29670" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29670-form-container" class="comment-form-container">
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

