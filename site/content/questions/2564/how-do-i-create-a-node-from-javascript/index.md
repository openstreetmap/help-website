+++
type = "question"
title = "How do I create a node from javascript?"
description = '''Hello community, I am trying to create POI nodes from javascript using AJAX requests (via a proxy) to talk to the API. My code to create a node looks like this: function osmNode(action, data){   var url = host + &quot;api/node.php&quot;;   var params = new Object();  params[&quot;action&quot;] = action;  params[&quot;change...'''
date = "2011-01-30T16:36:00Z"
lastmod = "2011-02-02T01:01:00Z"
weight = 2564
keywords = [ "node", "create", "javascript" ]
aliases = [ "/questions/2564" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I create a node from javascript?](/questions/2564/how-do-i-create-a-node-from-javascript)

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
<span id="post-2564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2564-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello community,</p>
<p>I am trying to create POI nodes from javascript using AJAX requests (via a proxy) to talk to the API. My code to create a node looks like this:</p>
<pre><code>function osmNode(action, data){
&#10;    var url =  host + &quot;api/node.php&quot;;
&#10;    var params = new Object();
    params[&quot;action&quot;] = action;
    params[&quot;changeset_id&quot;] = changeSetId;
    params[&quot;node_id&quot;] = nodeId;
    params[&quot;comment&quot;] = commentId;
    params[&quot;userName&quot;] = userName;
    params[&quot;userPassword&quot;] = pwd;
    params[&quot;data&quot;] = data;
&#10;    document.getElementById(&quot;saving&quot;).style.visibility = &quot;visible&quot;;
&#10;    $.ajax({
&#10;        url: url,
        type: &quot;GET&quot;,
        data: params,
        success: function(reqCode){
&#10;            var response = reqCode;
            switch (action){
                case &quot;create&quot;:
                    nodeId = trim(response);
                case &quot;move&quot;:
                case &quot;update&quot;:
                case &quot;delete&quot;:
                    updateOSM();
                    break;
            }
            document.getElementById(&quot;saving&quot;).style.visibility = &quot;collapse&quot;;
            return &quot;0&quot;;
        }
    });
}</code></pre>
<p>I call this with an action of "create" and the following XML for the node:</p>
<pre><code>&lt;?xml version=&#39;1.0&#39; encoding=&#39;UTF-8&#39;?&gt;
&lt;osm version=&quot;0.6&quot; generator=&quot;OpenStreetMap server&quot;&gt; 
&lt;node id=&quot;-1&quot; changeset=&quot;8151&quot; version=&quot;null&quot; lat=&quot;51.97096&quot; lon=&quot;7.70825&quot;&gt;
&lt;tag k=&quot;osmeditor:name&quot; v=&quot;Foo&quot;/&gt;
&lt;tag k=&quot;osmeditor:note&quot; v=&quot;Bar&quot;/&gt;
&lt;/node&gt;
&lt;/osm&gt;</code></pre>
<p>and it talks to my proxy which in turn talks to the API but instead of getting a new node ID back I get a message which reads:</p>
<pre><code>&lt;/osm&gt;. Fatal error: String not started expecting &#39; or &quot; at :1.</code></pre>
<p>Do you know this error ? Can anyone help ?</p>
<p>If you need to see the site, it is at <a href="http://www.uni-pages.de/projects/osm/index.php">http://www.uni-pages.de/projects/osm/index.php</a> and it is talking to the api06 test API.</p>
<p>greets Christian</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-create" rel="tag" title="see questions tagged &#39;create&#39;">create</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jan '11, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/236087acc7b2c4efe8f9810f454b9ae1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="paule85&#39;s gravatar image" />
<p><span>paule85</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="paule85 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Feb '11, 00:57</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-2564" class="comments-container">
&#10;</div>
<div id="comment-tools-2564" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2564-form-container" class="comment-form-container">
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

<span id="2670"></span>

<div id="answer-container-2670" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2670-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2670-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2670-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have stepped through your javascript in Firebug and traced the network traffic from my browser to your proxy, and from your proxy to the dev server and the problem seems to be with your proxy script.</p>
<p>Although the XML which leaves the browser looks like what you showed in the question, what arrives at the server looks like this:</p>
<pre><code>&lt;?xml version=\&#39;1.0\&#39; encoding=\&#39;UTF-8\&#39;?&gt;
&lt;osm version=\&quot;0.6\&quot; generator=\&quot;OpenStreetMap server\&quot;&gt; 
&lt;node id=\&quot;-1\&quot; changeset=\&quot;8151\&quot; version=\&quot;null\&quot; lat=\&quot;51.97096\&quot; lon=\&quot;7.70825\&quot;&gt;
&lt;tag k=\&quot;osmeditor:name\&quot; v=\&quot;Foo\&quot;/&gt;
&lt;tag k=\&quot;osmeditor:note\&quot; v=\&quot;Bar\&quot;/&gt;
&lt;/node&gt;
&lt;/osm&gt;</code></pre>
<p>As you can see, your proxy has escaped all the quotes. That causes the XML to fail to parse and the server to return this error:</p>
<pre><code>Cannot parse valid node from xml string &lt;?xml version=\&#39;1.0\&#39; encoding=\&#39;UTF-8\&#39;?&gt;
&lt;osm version=\&quot;0.6\&quot; generator=\&quot;OpenStreetMap server\&quot;&gt; 
&lt;node id=\&quot;-1\&quot; changeset=\&quot;8151\&quot; version=\&quot;null\&quot; lat=\&quot;51.97096\&quot; lon=\&quot;7.70825\&quot;&gt;
&lt;tag k=\&quot;osmeditor:name\&quot; v=\&quot;Foo\&quot;/&gt;
&lt;tag k=\&quot;osmeditor:note\&quot; v=\&quot;Bar\&quot;/&gt;
&lt;/node&gt;
&lt;/osm&gt;. Fatal error: String not started expecting &#39; or &quot; at :1.</code></pre>
<p>Unfortunately it looks like your proxy only returns the last line of that to the browser, hence the confusing error message in the browser.</p>
<p>I would also add that passing the XML as a URL parameter to the proxy is not really a good idea - it would be better to use POST and pass it in the body. Indeed as creating a node is not idempotent you should be using POST rather than GET for that request anyway.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Feb '11, 01:01</strong></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomH has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-2670" class="comments-container">
&#10;</div>
<div id="comment-tools-2670" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2670-form-container" class="comment-form-container">
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

