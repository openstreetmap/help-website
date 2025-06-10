+++
type = "question"
title = "Error while compiling OSRM Based Project"
description = '''Hi, I am trying to compile project which uses osrm libraries and was written in 2017.I installed osrm server on my system yesterday and trying to make the application run.But while compiling on ubuntu 18.04 i am getting compilation errors.For eg,for the following code block long long int OSRM_INTERF...'''
date = "2019-07-26T15:39:00Z"
lastmod = "2019-07-30T12:24:00Z"
weight = 70206
keywords = [ "compile", "osrm", "error" ]
aliases = [ "/questions/70206" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Error while compiling OSRM Based Project](/questions/70206/error-while-compiling-osrm-based-project)

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
<span id="post-70206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70206-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am trying to compile project which uses osrm libraries and was written in 2017.I installed osrm server on my system yesterday and trying to make the application run.But while compiling on ubuntu 18.04 i am getting compilation errors.For eg,for the following code block</p>
<pre><code>long long int OSRM_INTERFACE::viarouteCall(
        vector&lt;pair&lt;float, float&gt; &gt; locations) {
&#10;    // The following shows how to use the Route service; configure this service
    osrm::RouteParameters route_parameters;
    // route is in Monaco
    route_parameters.service = &quot;route&quot;;//route bateesh made chanfe from viaroutes to route
&#10;    for (unsigned int i = 0; i &lt; locations.size(); i++) {
&#10;        route_parameters.AddCoordinate(locations[i].first, locations[i].second);
    }
&#10;    osrm::json::Object json_result;
    const int result_code = (*routing_machine).RunQuery(route_parameters,
            json_result);
    //std::cout &lt;&lt; &quot;result code: &quot; &lt;&lt; result_code &lt;&lt; std::endl;
&#10;    long long int duration = 0;
&#10;    // 2xx code
&#10;    if (result_code / 100 == 2) {
        // Extract data out of JSON structure
        auto&amp; summary = json_result.values[&quot;route_summary&quot;].get&lt;
                osrm::json::Object&gt;();
        duration = summary.values[&quot;total_time&quot;].get&lt;osrm::json::Number&gt;().value;
//      auto distance =
//              summary.values[&quot;total_distance&quot;].get&lt;osrm::json::Number&gt;().value;
//      //std::cout &lt;&lt; &quot;duration: &quot; &lt;&lt; duration &lt;&lt; std::endl;
        //std::cout &lt;&lt; &quot;distance: &quot; &lt;&lt; distance &lt;&lt; std::endl;
    }
    //delete osrm;
    return duration;
}</code></pre>
<p>I am getting error during compilation like:-</p>
<pre><code>error: ‘struct osrm::engine::api::RouteParameters’ has no member named ‘service’; did you mean ‘overview’?
  route_parameters.service = &quot;viaroute&quot;;
                   ^~~~~~~
                   overview
src/osrm_interface.cpp:47:20: error: ‘struct osrm::engine::api::RouteParameters’ has no member named ‘AddCoordinate’; did you mean ‘coordinates’?
   route_parameters.AddCoordinate(locations[i].first, locations[i].second);
                    ^~~~~~~~~~~~~
                    coordinates
src/osrm_interface.cpp:51:45: error: ‘class osrm::OSRM’ has no member named ‘RunQuery’
  const int result_code = (*routing_machine).RunQuery(route_parameters,</code></pre>
<p>It seems to me as some API has changed and my machine is using new APIs and the code is built on old API.Can you tell me how can I see which parameters changes if i am correct?How do I make changes in the current code to use member names of new API?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jul '19, 15:39</strong></p>
<img src="https://secure.gravatar.com/avatar/75e1c27daf9b623af26e289ed62e48f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bateesh&#39;s gravatar image" />
<p><span>bateesh</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bateesh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jul '19, 08:18</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-70206" class="comments-container">
&#10;</div>
<div id="comment-tools-70206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70206-form-container" class="comment-form-container">
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

<span id="70209"></span>

<div id="answer-container-70209" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70209-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SimonPoole has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your question would seem to be rather out of scope for this site, I would suggest posing your question on the <a href="https://lists.openstreetmap.org/pipermail/osrm-talk/">OSRM mailing list</a> that is likely to get you faster and better results.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jul '19, 20:27</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-70209" class="comments-container">
<span id="70237"></span>
<div id="comment-70237" class="comment">
<div id="post-70237-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you.I have posted it there</p>
</div>
<div id="comment-70237-info" class="comment-info">
<span class="comment-age">(30 Jul '19, 10:02)</span> <span class="comment-user userinfo">bateesh</span>
</div>
</div>
<span id="70238"></span>
<div id="comment-70238" class="comment">
<div id="post-70238-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In case anyone is searching for it: <a href="https://lists.openstreetmap.org/pipermail/osrm-talk/2019-July/001790.html">https://lists.openstreetmap.org/pipermail/osrm-talk/2019-July/001790.html</a></p>
</div>
<div id="comment-70238-info" class="comment-info">
<span class="comment-age">(30 Jul '19, 12:24)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-70209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70209-form-container" class="comment-form-container">
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

