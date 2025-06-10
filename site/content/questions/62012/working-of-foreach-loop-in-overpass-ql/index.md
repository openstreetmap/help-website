+++
type = "question"
title = "Working of foreach loop in Overpass QL"
description = '''Dear All, This is with reference to the explanation of foreach loop in Overpass QL on the following page: query about foreach loop Query 1: Inside foreach loop, does ._ refer to one item in the set _ in the global namespace?  For example in this snippet: way[name=&quot;Foo&quot;];  foreach(  (  ._;  &amp;gt;;  );...'''
date = "2018-02-08T10:43:00Z"
lastmod = "2018-02-08T10:43:00Z"
weight = 62012
keywords = [ "overpass-ql", "loop" ]
aliases = [ "/questions/62012" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Working of foreach loop in Overpass QL](/questions/62012/working-of-foreach-loop-in-overpass-ql)

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
<span id="post-62012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62012-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear All,</p>
<p>This is with reference to the explanation of foreach loop in Overpass QL on the following page: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#For-each_loop_.28foreach.29">query about foreach loop</a></p>
<p>Query 1:</p>
<p>Inside foreach loop, does ._ refer to one item in the set _ in the global namespace?</p>
<p>For example in this snippet:</p>
<pre><code>way[name=&quot;Foo&quot;];
  foreach(
    (
      ._;
      &gt;;
    );
    out;
  );</code></pre>
<p>Here way[name="Foo"]; will put every way with the name ="Foo" in the default set _ . Then foreach will loop over each way in _ ( the global default set) and at each iteration of the foreach loop ._ (inside the foreach loop) refers to ONE way with the name ="Foo" ie ONE way in the global default set.It is taking the union of that ONE way with the nodes constituting that particular way.</p>
<p>Whereas in the following code:</p>
<pre><code>way[name=&quot;Foo&quot;];
(._;&gt;;);
out;</code></pre>
<p>Out here ._ is the set containing ALL the ways with name="Foo".</p>
<p>Do I understand correctly? The meaning of ._ is different when it is within the foreach loop and when it is outside the foreach loop. Is that correct? Its something like a global vs a local variable.</p>
<p>Query 2: In this snippet :</p>
<pre><code>way[name=&quot;Foo&quot;];
  foreach(
    (
      ._;
      &gt;;
    );
    out;
  );</code></pre>
<p>The foreach will loop over the global _ and put each way in the global _ in _ (which is local to the foreach) and place the result of (union of local _ and it's nodes ) (._ ;&gt;;); in _ which is local to the foreach and is NOT the global default set. The out will refer to this local _ and print out the contents of the local _ . Is this correct?</p>
<p>Query 3:</p>
<p>It says that the following snippet of code (from here, once again link:<a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#For-each_loop_.28foreach.29">query about foreach loop</a>):-</p>
<pre><code>way[name=&quot;Foo&quot;];
  foreach(
    (
      ._;
      &gt;;
    );
    out;
  );</code></pre>
<p>will do the following:</p>
<p>For each way that has a name tag with value "Foo", this prints the nodes that belong to this way immediately followed by the way itself.</p>
<p>I think the order is the other way round. It seems to me that it will first print each way with the name tag with value Foo and then print the nodes that belong to this way. Reason : inside the union in foreach loop we have (._;&gt;;); which FIRST has the way and THEN the nodes and not the other way round. Have I misunderstood how this works?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span> <span class="post-tag tag-link-loop" rel="tag" title="see questions tagged &#39;loop&#39;">loop</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '18, 10:43</strong></p>
<img src="https://secure.gravatar.com/avatar/514d8729582ac1f9386d46e13aa0050d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ashimkapoor&#39;s gravatar image" />
<p><span>ashimkapoor</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ashimkapoor has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Feb '18, 10:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-62012" class="comments-container">
&#10;</div>
<div id="comment-tools-62012" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62012-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

