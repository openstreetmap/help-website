+++
type = "question"
title = "How to send request to server to create a way with nodes that do not exist"
description = '''I&#x27;m developing some Android software using openstreetmap, and I&#x27;ve got a question:  I&#x27;d like to submit XML data to the server to create a way, but it always sends back the response &quot;Precondition Failed&quot;. I understand the error message - it means when the way has nodes that do not exist yet. But sure...'''
date = "2012-09-04T03:47:00Z"
lastmod = "2012-09-08T12:06:00Z"
weight = 15776
keywords = [ "api", "precondition_failed", "way" ]
aliases = [ "/questions/15776" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to send request to server to create a way with nodes that do not exist](/questions/15776/how-to-send-request-to-server-to-create-a-way-with-nodes-that-do-not-exist)

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
<span id="post-15776-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15776-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15776-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm developing some Android software using openstreetmap, and I've got a question:</p>
<p>I'd like to submit XML data to the server to create a way, but it always sends back the response "<code>Precondition Failed</code>". I understand the error message - it means when the way has nodes that do not exist yet.</p>
<p>But surely, the nodes of way do not already exist when i create a way? So I don't know how to solve the problem. I've read the API documentation many times and am trying to do the same as it shows in the examples.</p>
<p>Can you help me to solve the problem, or tell me the right way to send a request to server to create a way with nodes that do not yet exist?</p>
<p>Thank you very much!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-precondition_failed" rel="tag" title="see questions tagged &#39;precondition_failed&#39;">precondition_failed</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Sep '12, 03:47</strong></p>
<img src="https://secure.gravatar.com/avatar/0d3f1d803cb1a81267a0f74d6a7e7d38?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lovepanmei&#39;s gravatar image" />
<p><span>lovepanmei</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lovepanmei has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Sep '12, 10:08</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-15776" class="comments-container">
<span id="15777"></span>
<div id="comment-15777" class="comment">
<div id="post-15777-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you explain a bit more about the purpose of your application?</p>
</div>
<div id="comment-15777-info" class="comment-info">
<span class="comment-age">(04 Sep '12, 07:02)</span> <span class="comment-user userinfo">mmehl</span>
</div>
</div>
<span id="15789"></span>
<div id="comment-15789" class="comment">
<div id="post-15789-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'd also mention the "if you want to test your software" section of <a href="https://wiki.openstreetmap.org/wiki/API_v0.6">this page</a>. There's a copy of the API at <a href="http://api06.dev.openstreetmap.org/">http://api06.dev.openstreetmap.org/</a> which you can use for testing, which avoids filling the live database with rubbish.</p>
</div>
<div id="comment-15789-info" class="comment-info">
<span class="comment-age">(04 Sep '12, 10:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="15899"></span>
<div id="comment-15899" class="comment">
<div id="post-15899-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I know it ,but the request i submit probably has something wrong,but i don't know where.Can you help me to check the xml file as following: &lt;?xml version='1.0' encoding='UTF-8' standalone='yes' ?&gt;&lt;osm&gt;&lt;node id="-1" lat="34.23294236166552" lon="108.91146183013916" changeset="13030131"/&gt;&lt;node id="-2" lat="34.232294838724385" lon="108.9129638671875" changeset="13030131"/&gt;&lt;way changeset="13030131"&gt;&lt;tag k="name" v="hrllo"/&gt;&lt;tag k="RAILWAY" v="railway_platform"/&gt;&lt;nd ref="-1"/&gt;&lt;nd ref="-2"/&gt;&lt;/way&gt;&lt;/osm&gt;</p>
</div>
<div id="comment-15899-info" class="comment-info">
<span class="comment-age">(08 Sep '12, 06:46)</span> <span class="comment-user userinfo">lovepanmei</span>
</div>
</div>
</div>
<div id="comment-tools-15776" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15776-form-container" class="comment-form-container">
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

<span id="15902"></span>

<div id="answer-container-15902" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15902-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-15902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you've not tried <a href="http://www.wireshark.org/">Wireshark</a> you might find it of use. I just used JOSM to upload a hedge I traced from Bing and captured what was happening. The XML was:</p>
<pre><code>&lt;osmChange version=&quot;0.6&quot; generator=&quot;JOSM&quot;&gt;
&lt;create&gt;
  &lt;node id=&#39;-7352&#39; action=&#39;modify&#39; visible=&#39;true&#39; changeset=&#39;13030870&#39; lat=&#39;51.798472312219666&#39; lon=&#39;1.0875406870349713&#39; /&gt;
  &lt;node id=&#39;-7351&#39; action=&#39;modify&#39; visible=&#39;true&#39; changeset=&#39;13030870&#39; lat=&#39;51.79929719724354&#39; lon=&#39;1.0872364754165609&#39; /&gt;
  &lt;way id=&#39;-7353&#39; action=&#39;modify&#39; visible=&#39;true&#39; changeset=&#39;13030870&#39;&gt;
    &lt;nd ref=&#39;-7351&#39; /&gt;
    &lt;nd ref=&#39;-7352&#39; /&gt;
    &lt;tag k=&#39;barrier&#39; v=&#39;hedge&#39; /&gt;
    &lt;tag k=&#39;source&#39; v=&#39;bing&#39; /&gt;
  &lt;/way&gt;
&lt;/create&gt;
&lt;/osmChange&gt;</code></pre>
<p>So it looks like you create the nodes and then the ways in the same changeset.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Sep '12, 08:58</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Sep '12, 08:59</strong> </span></p>
</div>
</div>
<div id="comments-container-15902" class="comments-container">
<span id="15903"></span>
<div id="comment-15903" class="comment">
<div id="post-15903-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is the action that create the nodes and ways in the same chageset wrong?</p>
</div>
<div id="comment-15903-info" class="comment-info">
<span class="comment-age">(08 Sep '12, 09:14)</span> <span class="comment-user userinfo">lovepanmei</span>
</div>
</div>
<span id="15904"></span>
<div id="comment-15904" class="comment">
<div id="post-15904-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, if you look at EdLoach's osmChange XML above you'll see that's exactly what JOSM is doing. If you compare that XML with the XML that you're sending you may be able to see what you're doing wrong.</p>
</div>
<div id="comment-15904-info" class="comment-info">
<span class="comment-age">(08 Sep '12, 12:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-15902" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15902-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15778"></span>

<div id="answer-container-15778" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15778-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can not create a way with nodes that does not exist, or delete nodes when a way refers to it. This is to prevent the data from becoming inconsistant. You have to create the nodes before you create the way, or prefrebly at the same time.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '12, 07:13</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-15778" class="comments-container">
<span id="15781"></span>
<div id="comment-15781" class="comment">
<div id="post-15781-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>how can i create them at the same time?The data i submit include the way data and the node data also ,it remains wrong ,can you tell me the right xml format.I read the api many times.The time of my project is tight ,so please help.</p>
</div>
<div id="comment-15781-info" class="comment-info">
<span class="comment-age">(04 Sep '12, 07:40)</span> <span class="comment-user userinfo">lovepanmei</span>
</div>
</div>
<span id="15782"></span>
<div id="comment-15782" class="comment">
<div id="post-15782-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Would you show us a small XML with a way and only a few nodes that doesn't work?</p>
</div>
<div id="comment-15782-info" class="comment-info">
<span class="comment-age">(04 Sep '12, 07:42)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="15783"></span>
<div id="comment-15783" class="comment">
<div id="post-15783-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>&lt;osmchange version="0.6" generator="Osmosis"&gt; &lt;create&gt; &lt;node id="-1" timestamp="2007-01-02T00:00:00.0+11:00" lat="-33.9133118622908" lon="151.117335519304" changeset="1234" version="12"/&gt; &lt;node id="-2" timestamp="2007-01-02T00:00:00.0+11:00" lat="-33.9133118622911" lon="151.117335519312" changeset="1234" version="12"/&gt;</p>
<pre><code>   &lt;way id=&quot;-3&quot; timestamp=&quot;2007-01-02T00:00:00.0+11:00&quot; changeset=&quot;1234&quot; version=&quot;32&quot;&gt;
       &lt;nd ref=&quot;-1&quot;/&gt;
       &lt;nd ref=&quot;-2&quot;/&gt;
   &lt;/way&gt;</code></pre>
<p>&lt;/create&gt; &lt;/osmchange&gt; what i submit is like above,is there something wrong with it?</p>
</div>
<div id="comment-15783-info" class="comment-info">
<span class="comment-age">(04 Sep '12, 08:00)</span> <span class="comment-user userinfo">lovepanmei</span>
</div>
</div>
<span id="15797"></span>
<div id="comment-15797" class="comment">
<div id="post-15797-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If you are creating a node (using &lt;create&gt; and specifying a negative id), you don't need the version or timestamp just the lon, lat and changeset.</p>
<p>If you are trying to include an existing node (which is what version 12 suggests), don't try to create it just refer to its existing node id.</p>
</div>
<div id="comment-15797-info" class="comment-info">
<span class="comment-age">(04 Sep '12, 17:00)</span> <span class="comment-user userinfo">ChrisH</span>
</div>
</div>
<span id="15898"></span>
<div id="comment-15898" class="comment">
<div id="post-15898-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>if i want to create a way including not existing node ,how can i do? Is the following xml right? &lt;?xml version='1.0' encoding='UTF-8' standalone='yes' ?&gt; &lt;osm&gt; &lt;node id="-1" lat="34.23294236166552" lon="108.91146183013916" changeset="13030131"/&gt; &lt;node id="-2" lat="34.232294838724385" lon="108.9129638671875" changeset="13030131"/&gt; &lt;way changeset="13030131"&gt; &lt;tag k="name" v="hrllo"/&gt; &lt;tag k="RAILWAY" v="railway_platform"/&gt; &lt;nd ref="-1"/&gt; &lt;nd ref="-2"/&gt; &lt;/way&gt; &lt;/osm&gt;</p>
</div>
<div id="comment-15898-info" class="comment-info">
<span class="comment-age">(08 Sep '12, 06:43)</span> <span class="comment-user userinfo">lovepanmei</span>
</div>
</div>
</div>
<div id="comment-tools-15778" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15778-form-container" class="comment-form-container">
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

