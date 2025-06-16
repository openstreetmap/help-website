+++
type = "question"
title = "missing way in a relation"
description = '''I am new to OSM data. I downloaded city of Olathe (kansas/USA) OSM file olathe.osm. In it, looking at a relationID = 94008, it lists 313 ways as references. Many of these ways are not in this file as ways. For example, none of these wayID&#x27;s are in this OSM file. (13033282,13033261,110134331). Aren&#x27;t...'''
date = "2012-10-30T20:41:00Z"
lastmod = "2012-11-01T17:16:00Z"
weight = 17311
keywords = [ "osm", "relation", "missing" ]
aliases = [ "/questions/17311" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [missing way in a relation](/questions/17311/missing-way-in-a-relation)

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
<span id="post-17311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17311-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am new to OSM data. I downloaded city of Olathe (kansas/USA) OSM file olathe.osm. In it, looking at a relationID = <a href="https://www.openstreetmap.org/browse/relation/94008">94008</a>, it lists 313 ways as references. Many of these ways are not in this file as ways. For example, none of these wayID's are in this OSM file. (<a href="https://www.openstreetmap.org/browse/way/13033282">13033282</a>,<a href="https://www.openstreetmap.org/browse/way/13033261">13033261</a>,<a href="https://www.openstreetmap.org/browse/way/110134331">110134331</a>). Aren't all reference ways for a given relation suppose to be in this OSM raw data file as ways? Am I missing something?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Oct '12, 20:41</strong></p>
<img src="https://secure.gravatar.com/avatar/343237842fce1f7a82f69ebf7a92f6b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kcjailbirds&#39;s gravatar image" />
<p><span>kcjailbirds</span><br />
<span class="score" title="141 reputation points">141</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kcjailbirds has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Nov '12, 15:06</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-17311" class="comments-container">
<span id="17313"></span>
<div id="comment-17313" class="comment">
<div id="post-17313-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much. Two more questions! Where do I download the full extension OSM file for Germany! and also, is there a better way of doing what I am doing? What I need, is all the biclycle routes. So, I search the relations with any route tag = 'bicycle' and then try to get all the ways and all the nodes for each way. Is there a better way? I need to get all the routes for bicycle, hiking, etc...</p>
<p>of course programatically! I read all the nodes, ways, and relations into a sql server data structure that includes all their relationships.</p>
<p>Thank you very much</p>
</div>
<div id="comment-17313-info" class="comment-info">
<span class="comment-age">(30 Oct '12, 21:09)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
<span id="17338"></span>
<div id="comment-17338" class="comment">
<div id="post-17338-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have downloaded the germany.osm from geofabrik but it is not complete! It does not have all the nodes or ways that are listed as refrence node/ways for a given relation. Been looking at the overpass API but not been able to figure out what the proper query would be to give me all the nodes, ways, relations that have key/value pair of route/bicycle. Trying to get all the nodes, ways that comprise the bicycle routes in germany. This is what I tried in the overpass API query:</p>
<p>&lt;union&gt; &lt;query type="relation"&gt; &lt;has-kv k="route" v="bicycle"/&gt; &lt;/query&gt; &lt;recurse type="relation-node" into="nodes"/&gt; &lt;recurse type="relation-way"/&gt; &lt;recurse type="way-node"/&gt; &lt;/union&gt; &lt;print/&gt;</p>
<p>the file returned is blank. Any idea anyone?</p>
</div>
<div id="comment-17338-info" class="comment-info">
<span class="comment-age">(31 Oct '12, 20:02)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
<span id="17343"></span>
<div id="comment-17343" class="comment">
<div id="post-17343-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you give an example missing node or way? That might help us to understand what's going on.</p>
</div>
<div id="comment-17343-info" class="comment-info">
<span class="comment-age">(31 Oct '12, 22:58)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="17355"></span>
<div id="comment-17355" class="comment">
<div id="post-17355-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here is another example. I downloaded berlin.osm from geofabrik and it shows a relation with ID = <a href="https://www.openstreetmap.org/browse/relation/9030">9030</a> as a bicycle route with 514 nodes and ways. many of those ways are not downloaded in the same berlin.osm file. For example, wayid = <a href="https://www.openstreetmap.org/browse/way/26135363">26135363</a> and <a href="https://www.openstreetmap.org/browse/way/26135342">26135342</a> are not in this download. I can get each way individually but wanted to know how I can get a download that would have all bicycle routes for germany or a city in germany and all the ways that comprise the routes and all the nodes that comprise each way.</p>
<p>Thanks</p>
</div>
<div id="comment-17355-info" class="comment-info">
<span class="comment-age">(01 Nov '12, 13:34)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
<span id="17358"></span>
<div id="comment-17358" class="comment">
<div id="post-17358-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looking at that relation (a cycle route taking in some of the old Berlin Wall route) it does seem to cross over in Potsdam. Presumably the ways that you're interested in would be in the "germany.osm" that you've already downloaded?</p>
</div>
<div id="comment-17358-info" class="comment-info">
<span class="comment-age">(01 Nov '12, 15:10)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="17359"></span>
<div id="comment-17359" class="comment not_top_scorer">
<div id="post-17359-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Those two ways listed above I can find in germany.osm but not berlin.osm. However, another example, relation 14613, I can find wayid = 188044903 in the berlin.osm but not in germany.osm. So, I dont know which one to look at. Is there a way to download one file that has all bicycle routes including all ways, relations, and nodes that create those routes for a particular area like Berlin?</p>
</div>
<div id="comment-17359-info" class="comment-info">
<span class="comment-age">(01 Nov '12, 16:06)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
<span id="17363"></span>
<div id="comment-17363" class="comment not_top_scorer">
<div id="post-17363-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please avoid starting a long discussion about your topic on this FAQ site by adding more and more answers by yourself that are new questions ins reality. Try the comment feature instead.</p>
<p>I will try to convert your "answers" to comments later.</p>
<p>Or if you are dealing with regions within Germany and also you are speaking German, I reccomend the German sub-forum at <a href="http://forum.osm.org">http://forum.osm.org</a></p>
<p>Greets.</p>
</div>
<div id="comment-17363-info" class="comment-info">
<span class="comment-age">(01 Nov '12, 16:54)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="17364"></span>
<div id="comment-17364" class="comment not_top_scorer">
<div id="post-17364-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>According to <a href="https://www.openstreetmap.org/browse/way/188044903/history">its history page</a>, way 188044903 was created on Sun, 28 Oct 2012 10:31:27. Perhaps your "germany.osm" extract predates that?</p>
<p>To reiterate the answer, all bicycle routes that are wholly contained within Berlin will be within "berlin.osm". Bicycle routes that occur "in and around" Berlin won't necessarily be, but they will be within a recent "germany.osm".</p>
</div>
<div id="comment-17364-info" class="comment-info">
<span class="comment-age">(01 Nov '12, 17:16)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-17311" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-17311-form-container" class="comment-form-container">
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

<span id="17312"></span>

<div id="answer-container-17312" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17312-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17312-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17312-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kcjailbirds has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Relations can be large. By default all the ways and nodes that make up a relation are not downloaded. If you want all of the members you can use the full extension, in your case:</p>
<p><a href="https://www.openstreetmap.org/api/0.6/relation/94008/full">https://www.openstreetmap.org/api/0.6/relation/94008/full</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '12, 20:57</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-17312" class="comments-container">
&#10;</div>
<div id="comment-tools-17312" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17312-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17314"></span>

<div id="answer-container-17314" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17314-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-17314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can get the whole of Germany as an extract from <a href="http://download.geofabrik.de/openstreetmap/europe/">geofabrik</a>, or partial ones if that is easier. These are typically only a day old, so very useful. You might be able to extract the data you want from <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass</a>. The OSM API is primarily intended to support map editing. Overpass is a way to extract data without impacting the API and allows for much more flexible queries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '12, 21:37</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-17314" class="comments-container">
&#10;</div>
<div id="comment-tools-17314" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17314-form-container" class="comment-form-container">
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

