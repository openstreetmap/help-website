+++
type = "question"
title = "Count number of NWR per each of the input sets"
description = '''I have the follow Overpass Turbo query, and I would count number of NWR per each of the input sets. That is: 1) number of NWR for Trader Joe&#x27;s 2) number of NWR for Safeway I tried many times, and still not sure how to make it, can someone help please? [out:json][timeout:60]; (nwrbrand=&quot;Trader Joe&#x27;s&quot;...'''
date = "2021-02-06T07:53:00Z"
lastmod = "2021-02-08T09:38:00Z"
weight = 78690
keywords = [ "count", "inputset" ]
aliases = [ "/questions/78690" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Count number of NWR per each of the input sets](/questions/78690/count-number-of-nwr-per-each-of-the-input-sets)

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
<span id="post-78690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78690-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have the follow Overpass Turbo query, and I would count number of NWR per each of the input sets. That is: 1) number of NWR for Trader Joe's 2) number of NWR for Safeway I tried many times, and still not sure how to make it, can someone help please? [out:json][timeout:60]; (nwr<span>brand="Trader Joe's"</span>;)-&gt;.TJ; (nwr<span>brand="Safeway"</span>;)-&gt;.SW; (.TJ; .SW;); out skel center count;</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-count" rel="tag" title="see questions tagged &#39;count&#39;">count</span> <span class="post-tag tag-link-inputset" rel="tag" title="see questions tagged &#39;inputset&#39;">inputset</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Feb '21, 07:53</strong></p>
<img src="https://secure.gravatar.com/avatar/56979805fc55fa852c0708ba4abd8809?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steve_nonego&#39;s gravatar image" />
<p><span>steve_nonego</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steve_nonego has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78690" class="comments-container">
&#10;</div>
<div id="comment-tools-78690" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78690-form-container" class="comment-form-container">
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

<span id="78691"></span>

<div id="answer-container-78691" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78691-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use the <strong>make</strong> statement to create your own <em>count</em> elements:</p>
<pre><code>[out:json][timeout:60]; 
nwr[brand=&quot;Trader Joe&#39;s&quot;];
&#10;make count brand = set(t[&quot;brand&quot;]), 
           total = count(nwr);
out;
&#10;nwr[brand=&quot;Safeway&quot;];
&#10;make count brand = set(t[&quot;brand&quot;]), 
           total = count(nwr);
out;</code></pre>
<p>For further information: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#The_statement_make">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#The_statement_make</a></p>
<p>See also this <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Count_Pharmacies_per_County_.28updated_0.7.54.29">example</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '21, 09:37</strong></p>
<img src="https://secure.gravatar.com/avatar/9c8957ccf79025bf749665ebec2bdfa2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MarcoR&#39;s gravatar image" />
<p><span>MarcoR</span><br />
<span class="score" title="687 reputation points">687</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MarcoR has 5 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-78691" class="comments-container">
<span id="78713"></span>
<div id="comment-78713" class="comment">
<div id="post-78713-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/6765/marcor"></a><a href="https://help.openstreetmap.org/users/6765/marcor">@MarcoR</a> Thanks for you solution, it does what I expected!</p>
<p>I look up the links you recommend, yet I still not fully understand the query. Can you help me to understand the following?</p>
<p>For: nwr<span>brand="Trader Joe's"</span>;</p>
<p>make count brand = set(t["brand"]), total = count(nwr); out;</p>
<p>1) We didn't give the nwr[] a input set name, so it's automatically assume the set( ) is refer to the one above?</p>
<p>2) I look up the examples, it also use t["xxxx"], what is the t refer to? tag?</p>
<p>Last but not least, I slightly modified the query as:</p>
<p>[out:json][timeout:60];</p>
<p>nwr<span>brand="Trader Joe's"</span>; make count category = set("Number of Trader's"), total = count(nwr); out;</p>
<p>nwr<span>brand="Safeway"</span>; make count brand = set("Number of Safeway"), total = count(nwr); out;</p>
</div>
<div id="comment-78713-info" class="comment-info">
<span class="comment-age">(07 Feb '21, 19:33)</span> <span class="comment-user userinfo">steve_nonego</span>
</div>
</div>
<span id="78721"></span>
<div id="comment-78721" class="comment">
<div id="post-78721-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You are welcome ;)</p>
<p>1) The input set, if not specified, is the default one: <em>_</em>; as far as I undestand, nwr[…], doesn't have an input set as all it does is searching data in the map database, but it has an output set, which is <em>_</em>; this set is used as input set by the following command (make …); the next nwr[…] overwrites the default set with the new results so that the following 'make' statament can calculate the proper results;</p>
<p>2) t["xxx"] returns the value of the tag "xxx"; see <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Tag_Value_and_Generic_Value_Operators">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Tag_Value_and_Generic_Value_Operators</a></p>
<p>Hope this helps!</p>
</div>
<div id="comment-78721-info" class="comment-info">
<span class="comment-age">(08 Feb '21, 09:38)</span> <span class="comment-user userinfo">MarcoR</span>
</div>
</div>
</div>
<div id="comment-tools-78691" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78691-form-container" class="comment-form-container">
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

