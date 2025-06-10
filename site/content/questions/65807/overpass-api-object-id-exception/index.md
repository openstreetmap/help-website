+++
type = "question"
title = "Overpass API: Object ID-exception"
description = '''Hello, I want to use Overpass to find all Bars and Pubs around one kilometre of a coordinate. I have written there a code on overpass-turbo and tried it out: [out:json][timeout:25]; (  node(around:1000.0,54.3233417,10.1237456)[amenity~&quot;^(bar|pub)$&quot;]({{bbox}}); ); out body; &amp;gt;; out skel qt;  Now I ...'''
date = "2018-09-07T18:34:00Z"
lastmod = "2018-09-08T14:06:00Z"
weight = 65807
keywords = [ "overpassapi", "overpass", "overpass-turbo" ]
aliases = [ "/questions/65807" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass API: Object ID-exception](/questions/65807/overpass-api-object-id-exception)

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
<span id="post-65807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65807-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I want to use Overpass to find all Bars and Pubs around one kilometre of a coordinate. I have written there a code on overpass-turbo and tried it out:</p>
<pre><code>[out:json][timeout:25];
(
  node(around:1000.0,54.3233417,10.1237456)[amenity~&quot;^(bar|pub)$&quot;]({{bbox}});
);
out body;
&gt;;
out skel qt;</code></pre>
<p>Now I want to add an exception list for a few object and want to identify them by their Id. So I lokked up, if there is any option to solve it. I tried it to add these code:("id"!="2176294876") and other combinations and got always an error back.</p>
<p>Do you know any possibilities to solve this problem.</p>
<p>Thank you very much :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Sep '18, 18:34</strong></p>
<img src="https://secure.gravatar.com/avatar/0bee765aff7dbf52ca2df86cdb02ff2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Xadees&#39;s gravatar image" />
<p><span>Xadees</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Xadees has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65807" class="comments-container">
&#10;</div>
<div id="comment-tools-65807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65807-form-container" class="comment-form-container">
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

<span id="65821"></span>

<div id="answer-container-65821" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65821-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Xadees has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would put the ones you dont want into a set and use difference ( seta; - setb ) ;</p>
<pre><code>    [out:json][timeout:25];
    (
      node(around:1000.0,54.3233417,10.1237456)[amenity~&quot;^(bar|pub)$&quot;] ;
    ) -&gt; .possible ;
    (
    node ( 809743532) ;
    node ( 4449144065 ) ;
    ) -&gt; .unwanted;
    ( .possible ; - .unwanted ; ) ;
&#10;    out body;
    &gt;;
    out skel qt;</code></pre>
<p>In a bit more detail</p>
<ul>
<li><p>create a set <strong>.possible</strong> of all pubs</p>
<pre><code>(
  node(around:1000.0,54.3233417,10.1237456)[amenity~&quot;^(bar|pub)$&quot;] ;
) -&gt; .possible ;</code></pre></li>
<li><p>Create a set <strong>.unwanted</strong></p>
<pre><code>(
node ( 809743532) ;
node ( 4449144065 ) ;
) -&gt; .unwanted;</code></pre>
<ul>
<li><p>take the difference</p>
<p>( .possible ; - .unwanted ; ) ;</p></li>
</ul></li>
</ul>
<p>Note I have removed the <em>({{bbox}})</em> so I could find out where your points are and isn't needed with the <em>(around: )</em> clause.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Sep '18, 08:38</strong></p>
<img src="https://secure.gravatar.com/avatar/ba18d96cf193429ae1a16c30828ef58d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andrewblack&#39;s gravatar image" />
<p><span>andrewblack</span><br />
<span class="score" title="365 reputation points">365</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andrewblack has 4 accepted answers">57%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Sep '18, 08:45</strong> </span></p>
</div>
</div>
<div id="comments-container-65821" class="comments-container">
<span id="65826"></span>
<div id="comment-65826" class="comment">
<div id="post-65826-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for your fast answer. It is a nice solution and you explained it very well.</p>
</div>
<div id="comment-65826-info" class="comment-info">
<span class="comment-age">(08 Sep '18, 14:06)</span> <span class="comment-user userinfo">Xadees</span>
</div>
</div>
</div>
<div id="comment-tools-65821" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65821-form-container" class="comment-form-container">
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

