+++
type = "question"
title = "Create a &#x27;changeset&#x27; using api"
description = '''Hi, I&#x27;m creating a client for OSM api. I&#x27;m failing to create a changeset. (I&#x27;m using developers&#x27; url). I&#x27;m sending followings in header. oauth_token,oauth_consumer_key,oauth_signature_method,oauth_version,oauth_nonce,oauth_timestamp And message body as follows: &amp;lt;osm&amp;gt; &amp;lt;changeset&amp;gt;&amp;lt;tag k...'''
date = "2012-11-13T16:25:00Z"
lastmod = "2015-11-20T07:49:00Z"
weight = 17694
keywords = [ "oauth", "changeset", "api", "put", "client" ]
aliases = [ "/questions/17694" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Create a 'changeset' using api](/questions/17694/create-a-changeset-using-api)

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
<span id="post-17694-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17694-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17694-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm creating a client for OSM api. I'm failing to create a changeset. (I'm using developers' url). I'm sending followings in header. oauth_token,oauth_consumer_key,oauth_signature_method,oauth_version,oauth_nonce,oauth_timestamp And message body as follows:</p>
<pre><code>&lt;osm&gt;
&lt;changeset&gt;&lt;tag k=&quot;A&quot; v=&quot;Aaa&quot;/&gt;&lt;tag k=&quot;B&quot; v=&quot;Bbb&quot;/&gt;&lt;tag k=&quot;c&quot; v=&quot;Ccc&quot;/&gt;&lt;/changeset&gt;
&lt;changeset&gt;&lt;tag k=&quot;B&quot; v=&quot;Bbl&quot;/&gt;&lt;/changeset&gt;
&lt;changeset&gt;&lt;tag k=&quot;A&quot; v=&quot;Aab&quot;/&gt;&lt;tag k=&quot;F&quot; v=&quot;Afff&quot;/&gt;&lt;tag k=&quot;B&quot; v=&quot;bbb&quot;/&gt;&lt;/changeset&gt;
&lt;/osm&gt;</code></pre>
<p><strong>After sending data to server using PUT, I'm receiving http 500 response (Application error).</strong></p>
<p>Could someone help to solve this issue please?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-oauth" rel="tag" title="see questions tagged &#39;oauth&#39;">oauth</span> <span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-put" rel="tag" title="see questions tagged &#39;put&#39;">put</span> <span class="post-tag tag-link-client" rel="tag" title="see questions tagged &#39;client&#39;">client</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Nov '12, 16:25</strong></p>
<img src="https://secure.gravatar.com/avatar/658670034a8466e9db4fb65067d310f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="buddhima&#39;s gravatar image" />
<p><span>buddhima</span><br />
<span class="score" title="116 reputation points">116</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="buddhima has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Nov '12, 14:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span></p>
</div>
</div>
<div id="comments-container-17694" class="comments-container">
<span id="17707"></span>
<div id="comment-17707" class="comment">
<div id="post-17707-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Silly question : which URI are you using ? /api/0.6/changeset/create</p>
<p>Did you try first with only one &lt;changeset&gt; element ?</p>
</div>
<div id="comment-17707-info" class="comment-info">
<span class="comment-age">(14 Nov '12, 10:01)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="17708"></span>
<div id="comment-17708" class="comment">
<div id="post-17708-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi, url is <a href="http://api06.dev.openstreetmap.org/api/0.6/changeset/create">http://api06.dev.openstreetmap.org/api/0.6/changeset/create</a> Yes, I've tried with only one element too. But the result is same</p>
</div>
<div id="comment-17708-info" class="comment-info">
<span class="comment-age">(14 Nov '12, 10:05)</span> <span class="comment-user userinfo">buddhima</span>
</div>
</div>
</div>
<div id="comment-tools-17694" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17694-form-container" class="comment-form-container">
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

<span id="17720"></span>

<div id="answer-container-17720" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17720-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know exactly the reason for the 500 error code, but you are at least missing the <em>xml</em> tag. Here are the header and body of a <em>PUT</em> request to <em>/api/0.6/changeset/create</em> from a recent JOSM version:</p>
<p>header:</p>
<pre><code>PUT /api/0.6/changeset/create HTTP/1.1
User-Agent: JOSM/1.5 (5587 de)
Connection: close
Authorization: OAuth oauth_token=&quot;blah&quot;, oauth_consumer_key=&quot;blah&quot;, oauth_version=&quot;1.0&quot;, oauth_signature_method=&quot;HMAC-SHA1&quot;, oauth_timestamp=&quot;1353272088&quot;, oauth_nonce=&quot;blah&quot;, oauth_signature=&quot;blah&quot;
Content-type: text/xml
Host: api.openstreetmap.org
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2
Content-Length: 42</code></pre>
<p>body:</p>
<pre><code>&lt;?xml version=&#39;1.0&#39; encoding=&#39;UTF-8&#39;?&gt;
&lt;osm version=&#39;0.6&#39; generator=&#39;JOSM&#39;&gt;
  &lt;changeset  id=&#39;0&#39; open=&#39;false&#39;&gt;
    &lt;tag k=&#39;comment&#39; v=&#39;my changeset comment&#39; /&gt;
    &lt;tag k=&#39;created_by&#39; v=&#39;JOSM/1.5 (5581 en)&#39; /&gt;
  &lt;/changeset&gt;
&lt;/osm&gt;</code></pre>
<p>Also make sure to always include the <em>comment</em> and <em>created_by</em> tag in your changesets.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '12, 06:59</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Nov '12, 20:58</strong> </span></p>
</div>
</div>
<div id="comments-container-17720" class="comments-container">
<span id="17768"></span>
<div id="comment-17768" class="comment">
<div id="post-17768-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, In API spec. it is not mentioned to add xml tag. I failed even it is added. is it necessary to add version,generator attributes to osm tag? and id, open attributes in changeset tag?</p>
<p>I also would appriciate, if you can give me an example of PUT with headers too. (eg: Content-Type,etc.) Thanks!</p>
</div>
<div id="comment-17768-info" class="comment-info">
<span class="comment-age">(18 Nov '12, 19:06)</span> <span class="comment-user userinfo">buddhima</span>
</div>
</div>
<span id="17769"></span>
<div id="comment-17769" class="comment">
<div id="post-17769-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've added a header. You can use a program like wireshark or tcpdump yourself to read network packets of JOSM or other programs.</p>
<p>I'm not familiar with the API details so I can't say anything about which XML attributes are required and which not. Just try it if you can't find anything in the API documentation about this.</p>
</div>
<div id="comment-17769-info" class="comment-info">
<span class="comment-age">(18 Nov '12, 21:00)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-17720" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17720-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18457"></span>

<div id="answer-container-18457" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18457-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi All, Thanks for the help, specially scai. Message should follow following format in body.</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt; 
&lt;osm version=&quot;0.6&quot; generator=&quot;MyOpenstreetmapApp&quot;&gt; 
&lt;changeset&gt;
    &lt;tag k=&#39;comment&#39; v=&#39;my changeset comment&#39; /&gt;
    &lt;tag k=&#39;created_by&#39; v=&#39;JOSM/1.5 (5581 en)&#39; /&gt;   
&lt;/changeset&gt; 
&lt;/osm&gt;</code></pre>
<p>The above message format worked finally !</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '12, 15:50</strong></p>
<img src="https://secure.gravatar.com/avatar/658670034a8466e9db4fb65067d310f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="buddhima&#39;s gravatar image" />
<p><span>buddhima</span><br />
<span class="score" title="116 reputation points">116</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="buddhima has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Dec '12, 15:51</strong> </span></p>
</div>
</div>
<div id="comments-container-18457" class="comments-container">
&#10;</div>
<div id="comment-tools-18457" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18457-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17716"></span>

<div id="answer-container-17716" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17716-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The detail is on the <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Create:_PUT_.2Fapi.2F0.6.2Fchangeset.2Fcreate">wiki page</a>. You need to submit the page with an HTTP PUT.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '12, 20:28</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-17716" class="comments-container">
<span id="17717"></span>
<div id="comment-17717" class="comment">
<div id="post-17717-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, I was following that wiki page.But fails. can someone give me a full details of a successful http PUT request to OSM Thanks</p>
</div>
<div id="comment-17717-info" class="comment-info">
<span class="comment-age">(15 Nov '12, 03:40)</span> <span class="comment-user userinfo">buddhima</span>
</div>
</div>
<span id="17728"></span>
<div id="comment-17728" class="comment">
<div id="post-17728-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You may have an authentication problem. Check this page about OAuth in OSM : <a href="https://wiki.openstreetmap.org/wiki/OAuth">https://wiki.openstreetmap.org/wiki/OAuth</a></p>
</div>
<div id="comment-17728-info" class="comment-info">
<span class="comment-age">(15 Nov '12, 12:51)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="17751"></span>
<div id="comment-17751" class="comment">
<div id="post-17751-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, It's not a problem with authentication, since I'm getting a token and a secret after Access Token step. Thanks</p>
</div>
<div id="comment-17751-info" class="comment-info">
<span class="comment-age">(16 Nov '12, 14:11)</span> <span class="comment-user userinfo">buddhima</span>
</div>
</div>
<span id="46734"></span>
<div id="comment-46734" class="comment">
<div id="post-46734-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i have latitude and longitude of a location. i want to upload xml file about this location to add POI.where should i use lat and long? In changset?</p>
</div>
<div id="comment-46734-info" class="comment-info">
<span class="comment-age">(20 Nov '15, 05:42)</span> <span class="comment-user userinfo">Er Pawan Verma</span>
</div>
</div>
<span id="46735"></span>
<div id="comment-46735" class="comment">
<div id="post-46735-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/11577/er-pawan-verma"></a><a href="https://help.openstreetmap.org/users/11577/er-pawan-verma">@Er Pawan Verma</a>: to the node object. See the documentation for the API - e.g. <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Create:_PUT_.2Fapi.2F0.6.2F.5Bnode.7Cway.7Crelation.5D.2Fcreate">about nodes</a>. Please keep in mind that you should not create objects <a href="https://wiki.openstreetmap.org/wiki/Automated_edits">automatically</a>.</p>
</div>
<div id="comment-46735-info" class="comment-info">
<span class="comment-age">(20 Nov '15, 05:58)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="46736"></span>
<div id="comment-46736" class="comment not_top_scorer">
<div id="post-46736-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How can i put changeset? when i dont know.</p>
</div>
<div id="comment-46736-info" class="comment-info">
<span class="comment-age">(20 Nov '15, 06:02)</span> <span class="comment-user userinfo">Er Pawan Verma</span>
</div>
</div>
<span id="46743"></span>
<div id="comment-46743" class="comment not_top_scorer">
<div id="post-46743-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please don't hijack other people's question. Ask a new question instead (which you already did <a href="/questions/46741/using-put-api-http-authentication-to-upload-xml">here</a>).</p>
</div>
<div id="comment-46743-info" class="comment-info">
<span class="comment-age">(20 Nov '15, 07:49)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-17716" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-17716-form-container" class="comment-form-container">
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

