+++
type = "question"
title = "Extracting data values from OSRM&#x27;s osrm::json::object using C++"
description = '''I can receive the JSON result successfully and printing it to the console (as per the online samples), but I am have problems extracting actual field data. How can I extract individual fields as numbers, string, etc? I&#x27;ve tried various forms of casting, but this is what I have at the moment (trying ...'''
date = "2015-09-17T18:19:00Z"
lastmod = "2015-09-21T17:53:00Z"
weight = 45342
keywords = [ "osrm", "json", "c++" ]
aliases = [ "/questions/45342" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting data values from OSRM's osrm::json::object using C++](/questions/45342/extracting-data-values-from-osrms-osrmjsonobject-using-c)

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
<span id="post-45342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45342-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I can receive the JSON result successfully and printing it to the console (as per the online samples), but I am have problems extracting actual field data. How can I extract individual fields as numbers, string, etc?</p>
<p>I've tried various forms of casting, but this is what I have at the moment (trying to extract the status value):</p>
<pre><code>const int gr_result_code = routing_machine.RunQuery(route_parameters, json_result);
std::string sStat(&quot;status&quot;);
auto it = json_result.values.find(sStat);
osrm::json::Number vv =  (osrm::json::Number) ((*it).second); // doesn&#39;t compile
int v = (int) (vv.value); // probably some dodgy rounding here</code></pre>
<p>The Number casting is producing compiler errors. I guess I could convert the object to a string, and then using a third party JSON parser to extract individual fields, but this seems very wasteful.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-c++" rel="tag" title="see questions tagged &#39;c++&#39;">c++</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Sep '15, 18:19</strong></p>
<img src="https://secure.gravatar.com/avatar/86bccc1aafcdbecba3f3ea51162f3817?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="winwaed&#39;s gravatar image" />
<p><span>winwaed</span><br />
<span class="score" title="66 reputation points">66</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="winwaed has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-45342" class="comments-container">
&#10;</div>
<div id="comment-tools-45342" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45342-form-container" class="comment-form-container">
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

<span id="45483"></span>

<div id="answer-container-45483" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45483-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-45483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aseerel4c26 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With help from Daniel Hofman on the OSM listserver, I've managed to find the mapbox::util::get call, eg:</p>
<pre><code>    std::string sStat(&quot;status&quot;);
    auto it = json_result.values.find(sStat);
    double v = mapbox::util::get&lt;osrm::json::Number&gt;( (it-&gt;second) ).value;
&#10;    SimpleLogger().Write() &lt;&lt; &quot; status: &quot; &lt;&lt; v;</code></pre>
<p>(in this example, status only contains integer values, so it should also be rounded to an integer)</p>
<p>I think I need to read up on boost :-)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '15, 17:53</strong></p>
<img src="https://secure.gravatar.com/avatar/86bccc1aafcdbecba3f3ea51162f3817?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="winwaed&#39;s gravatar image" />
<p><span>winwaed</span><br />
<span class="score" title="66 reputation points">66</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="winwaed has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-45483" class="comments-container">
&#10;</div>
<div id="comment-tools-45483" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45483-form-container" class="comment-form-container">
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

