+++
type = "question"
title = "JSON from a xapi query ?"
description = '''So I am trying to get the maxspeed for a bounded box, a working example is this  www.overpass-api.de/api/xapi?[maxspeed=][bbox=-106.631425,52.078132,-106.566537,52.146866] However I am unable to get a JSON out of it. I have used the other way that is overpass ql like this  http://overpass-api.de/api...'''
date = "2014-12-03T21:49:00Z"
lastmod = "2014-12-05T15:15:00Z"
weight = 39026
keywords = [ "overpassapi", "overpass", "xapi", "overpass-ql" ]
aliases = [ "/questions/39026" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [JSON from a xapi query ?](/questions/39026/json-from-a-xapi-query)

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
<span id="post-39026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39026-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So I am trying to get the maxspeed for a bounded box, a working example is this www.overpass-api.de/api/xapi?<em>[maxspeed=</em>][bbox=-106.631425,52.078132,-106.566537,52.146866]</p>
<p>However I am unable to get a JSON out of it. I have used the other way that is overpass ql like this <a href="http://overpass-api.de/api/interpreter?data=%5Bout:json%5D;(node(52.078132,-106.631425,52.146866,-106.566537);%3C;);out">http://overpass-api.de/api/interpreter?data=[out:json];(node(52.078132,-106.631425,52.146866,-106.566537);&lt;;);out</a> body;</p>
<p>However the data returned isnt as consistent as I would like. Sometimes overpass ql returns the right data and sometimes it doesnt, while as xapi provides more consistency. Is there a way to get JSON using xapi ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Dec '14, 21:49</strong></p>
<img src="https://secure.gravatar.com/avatar/9893933c885520e100999425e74ae7ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="klk&#39;s gravatar image" />
<p><span>klk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="klk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-39026" class="comments-container">
<span id="39029"></span>
<div id="comment-39029" class="comment">
<div id="post-39029-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you describe what exactly about the data isn't consistent?</p>
</div>
<div id="comment-39029-info" class="comment-info">
<span class="comment-age">(04 Dec '14, 10:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="39042"></span>
<div id="comment-39042" class="comment">
<div id="post-39042-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For the bbox set of points, the overpass ql query did not spit out any information. While as when I used xapi there was data for those points. I thought they were accessing the same database.</p>
</div>
<div id="comment-39042-info" class="comment-info">
<span class="comment-age">(04 Dec '14, 18:20)</span> <span class="comment-user userinfo">klk</span>
</div>
</div>
</div>
<div id="comment-tools-39026" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39026-form-container" class="comment-form-container">
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

<span id="39030"></span>

<div id="answer-container-39030" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39030-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-39030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>First of all: XAPI does not support JSON at all. The follow answer will help you to create an equivalent Overpass XML / QL query which comes with JSON output. Use it as a replacement of your current XAPI query.</strong></p>
<p>If you prepend your XAPI query with "debug=", you can see the actual Overpass XML representation of the XAPI query. We use this as a starting point to create an equivalent query which returns JSON instead of XML. BTW: Internally, your XAPI query is converted into exactly this format before is it being executed by overpass api.</p>
<pre><code>http://www.overpass-api.de/api/xapi?debug=*[maxspeed=][bbox=-106.631425,52.078132,-106.566537,52.146866]</code></pre>
<p>Result:</p>
<pre><code>&lt;query type=&quot;node&quot;&gt;
  &lt;bbox-query s=&quot;52.078132&quot; n=&quot;52.146866&quot; w=&quot;-106.631425&quot; e=&quot;-106.566537&quot;/&gt;
  &lt;has-kv k=&quot;maxspeed&quot; v=&quot;&quot;/&gt;
&lt;/query&gt;
&lt;union&gt;
  &lt;item/&gt;
  &lt;query type=&quot;way&quot;&gt;
    &lt;bbox-query s=&quot;52.078132&quot; n=&quot;52.146866&quot; w=&quot;-106.631425&quot; e=&quot;-106.566537&quot;/&gt;
    &lt;has-kv k=&quot;maxspeed&quot; v=&quot;&quot;/&gt;
  &lt;/query&gt;
  &lt;recurse type=&quot;way-node&quot;/&gt;
&lt;/union&gt;
&lt;print/&gt;
&lt;query type=&quot;relation&quot;&gt;
  &lt;bbox-query s=&quot;52.078132&quot; n=&quot;52.146866&quot; w=&quot;-106.631425&quot; e=&quot;-106.566537&quot;/&gt;
  &lt;has-kv k=&quot;maxspeed&quot; v=&quot;&quot;/&gt;
&lt;/query&gt;
&lt;print/&gt;</code></pre>
<p>Now, we need to tell Overpass API to return the result in JSON format. This can be achieved by adding an osm-script header with a dedicated output attribute:</p>
<pre><code>&lt;osm-script output=&quot;json&quot;&gt;
...
&lt;/osm-script&gt;</code></pre>
<p>If you run this query, you will get exactly the same date as per your XAPI query, now with JSON format output. Try this in overpass turbo. <a href="http://overpass-turbo.eu/s/6nr">http://overpass-turbo.eu/s/6nr</a></p>
<p>If you favor Overpass QL format, you can easily convert your Overpass XML query by clicking on Export -&gt; Query -&gt; Overpass QL in overpass turbo. That's how this would look like.</p>
<pre><code>[out:json]
;
node
  (52.078132,-106.631425,52.146866,-106.566537)
  [&quot;maxspeed&quot;];
(
  ._;
  way
    (52.078132,-106.631425,52.146866,-106.566537)
    [&quot;maxspeed&quot;];
  node(w);
);
out;
relation
  (52.078132,-106.631425,52.146866,-106.566537)
  [&quot;maxspeed&quot;];
out;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Dec '14, 12:14</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Dec '14, 15:14</strong> </span></p>
</div>
</div>
<div id="comments-container-39030" class="comments-container">
<span id="39077"></span>
<div id="comment-39077" class="comment">
<div id="post-39077-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>when I have read the question right, he is looking for the RESULT in JSON format, and not the query itself, isn't it?</p>
</div>
<div id="comment-39077-info" class="comment-info">
<span class="comment-age">(05 Dec '14, 14:40)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="39082"></span>
<div id="comment-39082" class="comment">
<div id="post-39082-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/99/stephan75"></a><a href="http://help.openstreetmap.org/users/99/stephan75">@stephan75</a>: xapi is unable to produce JSON. My answer will help you to create an equivalent Overpass XML/QL query, which in fact returns the same result in JSON format.</p>
</div>
<div id="comment-39082-info" class="comment-info">
<span class="comment-age">(05 Dec '14, 15:15)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-39030" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39030-form-container" class="comment-form-container">
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

