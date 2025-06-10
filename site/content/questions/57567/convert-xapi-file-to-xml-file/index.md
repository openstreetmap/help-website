+++
type = "question"
title = "convert xapi file to xml file"
description = '''I&#x27;m making an http get request this way, in angular: this.http.get(&#x27;http://www.overpass-api.de/api/xapi?*[amenity=hospital][bbox=13.20524,43.70861,13.22842,43.72338]&#x27;) .subscribe( data =&amp;gt; {  console.log(data.toString());  });  but the following error is given: Cannot read property &#x27;toString&#x27; of n...'''
date = "2017-08-11T17:32:00Z"
lastmod = "2017-08-12T15:08:00Z"
weight = 57567
keywords = [ "angularjs" ]
aliases = [ "/questions/57567" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [convert xapi file to xml file](/questions/57567/convert-xapi-file-to-xml-file)

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
<span id="post-57567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57567-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm making an http get request this way, in angular:</p>
<pre><code>this.http.get(&#39;http://www.overpass-api.de/api/xapi?*[amenity=hospital][bbox=13.20524,43.70861,13.22842,43.72338]&#39;)
.subscribe(
data =&gt; {
    console.log(data.toString());
 });</code></pre>
<p>but the following error is given:</p>
<pre><code>Cannot read property &#39;toString&#39; of null</code></pre>
<p>I've also tried mapping the result this way:</p>
<pre><code>this.http.get(&#39;http://www.overpass-api.de/api/xapi?*[amenity=hospital][bbox=13.20524,43.70861,13.22842,43.72338]&#39;)
.map(res =&gt; res.toString())
.subscribe(
data =&gt; {
    console.log(data);
 });</code></pre>
<p>but the error remains. The xapi file I get if I go to <a href="http://www.overpass-api.de/api/xapi?*%5Bamenity=hospital%5D%5Bbbox=13.20524,43.70861,13.22842,43.72338%5D">http://www.overpass-api.de/api/xapi?*[amenity=hospital][bbox=13.20524,43.70861,13.22842,43.72338]</a> is not null, so I'm supposing the method can't read the xapi file. Is there a way I can convert it to xml file?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-angularjs" rel="tag" title="see questions tagged &#39;angularjs&#39;">angularjs</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Aug '17, 17:32</strong></p>
<img src="https://secure.gravatar.com/avatar/11a47a19b0ffc577a4a2354300a714aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PachiEPap&#39;s gravatar image" />
<p><span>PachiEPap</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PachiEPap has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57567" class="comments-container">
&#10;</div>
<div id="comment-tools-57567" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57567-form-container" class="comment-form-container">
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

<span id="58186"></span>

<div id="answer-container-58186" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58186-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The resulting file <em>is</em> a XML file. Just open the URL in your browser, save the file and open it in you favorite editor. Either a bug in your code. Or you have too many requests against this Overpass API server. In the latter case an error message will be returned. Either way, take a look at the content of the file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Aug '17, 08:59</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-58186" class="comments-container">
<span id="58267"></span>
<div id="comment-58267" class="comment">
<div id="post-58267-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The content of the file is ok as said, so I don't know why the method can't read it. I've tried using interpreter for obtaining a json output, using this: <a href="https://www.overpass-api.de/api/interpreter?data=%5Bout:json%5D;node%5Bamenity=bar%5D(43.70861,13.20524,43.72338,13.22842);out%20meta;"><code>https://www.overpass-api.de/api/interpreter?data=[out:json];node[amenity=bar](43.70861,13.20524,43.72338,13.22842);out%20meta;</code></a> Even now, in the browser the result is ok, but the same error is shown</p>
</div>
<div id="comment-58267-info" class="comment-info">
<span class="comment-age">(12 Aug '17, 12:27)</span> <span class="comment-user userinfo">PachiEPap</span>
</div>
</div>
<span id="58269"></span>
<div id="comment-58269" class="comment">
<div id="post-58269-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You need to ask somebody with angular.js as it is nearly sure that your code is broken.</p>
</div>
<div id="comment-58269-info" class="comment-info">
<span class="comment-age">(12 Aug '17, 15:08)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-58186" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58186-form-container" class="comment-form-container">
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

