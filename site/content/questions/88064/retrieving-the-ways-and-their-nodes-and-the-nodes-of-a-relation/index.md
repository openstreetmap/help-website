+++
type = "question"
title = "Retrieving the ways (and their nodes) and the nodes of a relation"
description = '''Hi, I have the following query which returns the boundary relation for Spain along with the ways it references and the nodes that these ways reference. area[&quot;ISO3166-1&quot;=&quot;ES&quot;][admin_level=2]; (relation[&quot;boundary&quot;=&quot;administrative&quot;][&quot;admin_level&quot;=&quot;2&quot;]&quot;name:en&quot;=&quot;Spain&quot;; way(r); node(w); );out; I get lot...'''
date = "2023-12-20T20:41:00Z"
lastmod = "2023-12-27T20:51:00Z"
weight = 88064
keywords = [ "overpass", "nodes", "relation" ]
aliases = [ "/questions/88064" ]
osqa_answers = 6
osqa_accepted = false
+++

<div class="headNormal">

# [Retrieving the ways (and their nodes) and the nodes of a relation](/questions/88064/retrieving-the-ways-and-their-nodes-and-the-nodes-of-a-relation)

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
<span id="post-88064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88064-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have the following query which returns the boundary relation for Spain along with the ways it references and the nodes that these ways reference. area["ISO3166-1"="ES"][admin_level=2]; (relation["boundary"="administrative"]["admin_level"="2"]<a href="area">"name:en"="Spain"</a>; way(r); node(w); );out; I get lots of ways and their nodes returned based on the members where type="way". I do not get the two member entries where type="node" though. I have tried adding node(r) to my query but doing this seems to block getting the ways. Is there a single query that will get me ways (and their nodes), and the member nodes of the relation? Many thanks, Chessel</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Dec '23, 20:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a7c7c42b3ace9de1b7d8fd5592ece3ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chessel&#39;s gravatar image" />
<p><span>Chessel</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chessel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88064" class="comments-container">
<span id="88078"></span>
<div id="comment-88078" class="comment">
<div id="post-88078-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You need to post the actual routine you ran as the code above has errors. Use code formatting &amp;/or post a link (use the Share button). What is it you're attempting to output. It's not very clear. Edit: I've simplified it a bit for you: <a href="https://overpass-turbo.eu/s/1Fc8">https://overpass-turbo.eu/s/1Fc8</a></p>
</div>
<div id="comment-88078-info" class="comment-info">
<span class="comment-age">(24 Dec '23, 15:05)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="88079"></span>
<div id="comment-88079" class="comment">
<div id="post-88079-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, my replying comment is too long so I'll will do an answer.</p>
</div>
<div id="comment-88079-info" class="comment-info">
<span class="comment-age">(24 Dec '23, 16:28)</span> <span class="comment-user userinfo">Chessel</span>
</div>
</div>
</div>
<div id="comment-tools-88064" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88064-form-container" class="comment-form-container">
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

6 Answers:

</div>

</div>

<span id="88080"></span>

<div id="answer-container-88080" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88080-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Dave, thanks for your answer. Sorry my question isn't clear. The reason why my question is formatted poorly is I'm not using the overpass web site as I'm a blind user and visual renderings of my results don't help me. I need to examine the results of my queries by looking at the raw data returned. So I make an http call to overpass in my browser which gets me a file back I can then analyze.</p>
<p>My aim is to download the relation that relates to a given country describing its border at admin level 2. The relation has &lt;member&gt; elements which reference nodes, ways and relations. I don't want the relations referenced here but I do want to retrieve the nodes referenced, plus the ways. And for those ways, I want to retrieve the nodes they reference.</p>
<p>My entire call is: <a href="http://overpass-api.de/api/interpreter?data=area%5B">http://overpass-api.de/api/interpreter?data=area["ISO3166-1"="ES"][admin_level=2];(relation["boundary"="administrative"]["admin_level"="2"]</a><a href="area">"name:en"="Spain"</a>;way(r);node(w););out;</p>
<p>The key parts are:</p>
<p>area["ISO3166-1"="ES"][admin_level=2];</p>
<p>(relation["boundary"="administrative"]["admin_level"="2"]<a href="area">"name:en"="Spain"</a>;</p>
<p>way(r);</p>
<p>node(w);</p>
<p>);</p>
<p>out;</p>
<p>At the moment, this query gets me the main relation for Spain, the ways it references, and the nodes these ways reference. It omits the nodes directly referenced by the relation in &lt;member&gt; tags. Okay, there are just two of them, but I still want them.</p>
<p>Hope this is clearer.</p>
<p>Kind regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Dec '23, 16:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a7c7c42b3ace9de1b7d8fd5592ece3ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chessel&#39;s gravatar image" />
<p><span>Chessel</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chessel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88080" class="comments-container">
&#10;</div>
<div id="comment-tools-88080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88080-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="88081"></span>

<div id="answer-container-88081" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88081-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This requires two separate replies as the problem may relate to other threads on github &amp; needs further investigation.</p>
<p>First post: syntax problems with your routine as is.</p>
<p>You have no square brackets around "name:en"=Spain; so your routine returns an error.</p>
<p>There is no requirement for [admin_level=2] as all ISO3166-1 areas are the same admin_level</p>
<p>area["ISO3166-1"=ES]; is the same as your second line so you're duplicating data.</p>
<p>Edit: Add 'geom' to the 'out': <a href="https://overpass-api.de/api/interpreter?data=area%5B">https://overpass-api.de/api/interpreter?data=area["ISO3166-1"=ES];(rel(pivot);way(r);node(w););out</a> geom;</p>
<p>Use either:</p>
<p>area["ISO3166-1"=ES];(rel(pivot);way(r);node(w););out;</p>
<p>or</p>
<p>(rel[boundary=administrative][admin_level=2]["name:en"=Spain];way(r);node(w););out;</p>
<p>Edit: Add 'geom' to the 'out': <a href="https://overpass-api.de/api/interpreter?data=area%5B">https://overpass-api.de/api/interpreter?data=area["ISO3166-1"=ES];(rel(pivot);way(r);node(w););out</a> geom;</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Dec '23, 22:04</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Dec '23, 22:38</strong> </span></p>
</div>
</div>
<div id="comments-container-88081" class="comments-container">
&#10;</div>
<div id="comment-tools-88081" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88081-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="88083"></span>

<div id="answer-container-88083" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88083-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88083-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88083-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Dave, Thanks for tidying up my query. I see how I was duplicating info in my request.</p>
<p>My original problem is still present however. The relation for Spain has ID 21068295. It references two nodes:</p>
<pre><code>&lt;member type=&quot;node&quot; ref=&quot;21068295&quot; role=&quot;admin_centre&quot;/&gt;
&#10;&lt;member type=&quot;node&quot; ref=&quot;148332300&quot; role=&quot;label&quot;/&gt;</code></pre>
<p>And these are not returned by the query.</p>
<p>I have tried adding node(r) but this makes no difference.</p>
<p>So is there a way to retrieve all the data the query currently does plus the &lt;node&gt; entries for the two nodes referenced directly by the member?</p>
<p>I also don't see the value in adding 'geom' to my out clause. It looks like it adds bounding box info but I'll be calculating these as my application interprets the XML data I retrieve.</p>
<p>Thank you for any further help you can give, Chessel</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Dec '23, 19:46</strong></p>
<img src="https://secure.gravatar.com/avatar/a7c7c42b3ace9de1b7d8fd5592ece3ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chessel&#39;s gravatar image" />
<p><span>Chessel</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chessel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88083" class="comments-container">
<span id="88084"></span>
<div id="comment-88084" class="comment">
<div id="post-88084-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>They are in mine:</p>
<p>&lt;member type="node" ref="21068295" role="admin_centre" lat="40.4167047" lon="-3.7035825"/&gt; &lt;member type="node" ref="148332300" role="label" lat="39.3260685" lon="-4.8379791"/&gt;</p>
<p>Are you sure you're copy pasting the url I gave you with geom at the end? The resulting file contains them. Search for just the ref value.</p>
</div>
<div id="comment-88084-info" class="comment-info">
<span class="comment-age">(26 Dec '23, 01:33)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-88083" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88083-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="88086"></span>

<div id="answer-container-88086" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88086-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello Dave,</p>
<p>I used the first variation you suggested and included the geom keyword. This downloads about 5.7Mb of xml compared to about 3.3Mb without the geom tag.</p>
<p>I don't see the two relation nodes, ref="21068295" and ref="148332300", except in the &lt;relation element="" itself.="" the="" geom="" keyword="" does="" mean="" the="" coordinates="" are="" also="" part="" of="" the="" &lt;member=""&gt; tag info for the nodes but not the node tags.</p>
<p>Looking at the whole file... finding the first node in the downloaded file with a tag is node with id="26864258". which has about 16 tags.</p>
<p>The whole download has a structure of nodes first, then ways, then the relation.</p>
<p>I'd like, if possible, to have the two nodes ref="21068295" and ref="148332300" included in the rest of the nodes area of the download.</p>
<p>If it isn't possible then so be it and I'll have to do a second call to get them but would be simpler to have everything for a relation come down in one call.</p>
<p>Kind regards, Chris</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '23, 10:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a7c7c42b3ace9de1b7d8fd5592ece3ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chessel&#39;s gravatar image" />
<p><span>Chessel</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chessel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88086" class="comments-container">
&#10;</div>
<div id="comment-tools-88086" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88086-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="88087"></span>

<div id="answer-container-88087" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88087-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>area["ISO3166-1"=ES];rel(pivot);(nw(r);node(w););out;</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '23, 13:33</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-88087" class="comments-container">
&#10;</div>
<div id="comment-tools-88087" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88087-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="88091"></span>

<div id="answer-container-88091" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88091-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88091-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88091-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Dave,</p>
<p>That works, thank you. I moved the rel(pivot) inside the brackets otherwise the relation itself wasn't downloaded. But now I get all the nodes and ways for the relation including the two nodes referenced by the relation directly.</p>
<p>Now all I need to do is debug my code which reads in this 3.3Mb of data so my laptop doesn't fall over because I allocate memory in an un-ending loop somewhere.</p>
<p>Thanks again, Chessel</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '23, 20:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a7c7c42b3ace9de1b7d8fd5592ece3ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chessel&#39;s gravatar image" />
<p><span>Chessel</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chessel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88091" class="comments-container">
&#10;</div>
<div id="comment-tools-88091" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88091-form-container" class="comment-form-container">
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

