+++
type = "question"
title = "how to retrieve multiple points from MongoDB and plot them on OSM?"
description = '''The data stored in my Database &quot;video&quot; of &quot;shows&quot; collection in mongodb is as this. It has 3 feilds as dose_rate, x, y. My code for &quot;app.js&quot; is as follows : var express=require(&#x27;express&#x27;); var MongoClient=require(&#x27;mongodb&#x27;).MongoClient; var engines=require(&#x27;consolidate&#x27;); var assert=require(&#x27;assert&#x27;...'''
date = "2017-02-15T06:19:00Z"
lastmod = "2017-02-15T06:19:00Z"
weight = 54642
keywords = [ "node", "mongodb", "html", "osm", "javascript" ]
aliases = [ "/questions/54642" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to retrieve multiple points from MongoDB and plot them on OSM?](/questions/54642/how-to-retrieve-multiple-points-from-mongodb-and-plot-them-on-osm)

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
<span id="post-54642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54642-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The data stored in my Database "video" of "shows" collection in mongodb is as <a href="https://i.stack.imgur.com/XQ7tF.jpg">this</a>. It has 3 feilds as dose_rate, x, y.</p>
<p>My code for "app.js" is as follows :</p>
<pre><code>var express=require(&#39;express&#39;);
var MongoClient=require(&#39;mongodb&#39;).MongoClient;
var engines=require(&#39;consolidate&#39;);
var assert=require(&#39;assert&#39;);
var app=express();
&#10;app.engine(&#39;html&#39;,engines.nunjucks);
app.set(&#39;view engine&#39;,&#39;html&#39;);
app.set(&#39;views&#39;,__dirname+ &#39;/views&#39;);
&#10;MongoClient.connect(&#39;mongodb://localhost:27017/video&#39;,function(err,db){
assert.equal(null,err);
console.log(&quot;successfully connect to the MongoDB server&quot;);
app.get(&#39;/&#39;,function(req,res){
    db.collection(&#39;shows&#39;).find({}).toArray(function(err,docs){
        res.render(&#39;shows&#39;,{&#39;shows&#39;:docs});
        });
      });
    });
 });
&#10;app.listen(4596,function(req,res){
console.log(&quot;connect to the port 4596&quot;);
});</code></pre>
<p>the below code is for "shows.html" :</p>
<pre><code>&lt;!DOCTYPE html&gt;
 &lt;html&gt;
&#10;&lt;head&gt;
&lt;title&gt;Plotting points&lt;/title&gt;
&lt;/head&gt;
&#10;&lt;body&gt;
&lt;ul class=&quot;nav navbar-nav&quot;&gt;
{%for show in shows%}
&lt;li&gt;{{show.dose_rate}}&lt;/li&gt;
&lt;li&gt; {{show.x}}&lt;/li&gt;
&lt;li&gt;{{show.y}}&lt;/li&gt;
{%endfor%}
&lt;/ul&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
<p>on running the code of "app.js" and on opening "shows.html" from browser on localhost, the output is that all points (i.e dose_rate, x, y) of my "shows" collection in "video" database is displayed on HTML page as <a href="https://i.stack.imgur.com/6LZTp.png">this</a>.</p>
<p>now i did get code for plotting a point on OSM as marker from this link--&gt; <a href="http://wiki.openstreetmap.org/wiki/OpenLayers_Simple_Example">wiki.openstreetmap.org/wiki/OpenLayers_Simple_Example</a> <strong>independently</strong> without app.js running in background as simple HTML page.</p>
<p><strong>I want to plot all my points stored in my collection "shows" as "x" and "y" from that db on OSM map, one by one, at once. I tried finding all reference to this problem but failed to find one. Please help me in doing so as i am new to OSM and nodejs or post any reference which i can read or tag someone who can help. THANK YOU IN ADVANCE</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-mongodb" rel="tag" title="see questions tagged &#39;mongodb&#39;">mongodb</span> <span class="post-tag tag-link-html" rel="tag" title="see questions tagged &#39;html&#39;">html</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Feb '17, 06:19</strong></p>
<img src="https://secure.gravatar.com/avatar/270d66b362f9140ec275bd66142ad01b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnnp&#39;s gravatar image" />
<p><span>pnnp</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnnp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54642" class="comments-container">
&#10;</div>
<div id="comment-tools-54642" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54642-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

