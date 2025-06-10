+++
type = "question"
title = "android phonegap changeset create"
description = '''Hi, I am developing an android app using phonegap apis. I would like the app to to upload map data to osm using the osm apiv0.6. iam using the code below from localhost to create a changeset:  function createChangeset(){  var xmlData = &#x27;&amp;lt;osm&amp;gt;&amp;lt;changeset&amp;gt;&amp;lt;tag k=&quot;created_by&quot; v=&quot;mappr&quot;/&amp;g...'''
date = "2012-04-12T10:16:00Z"
lastmod = "2012-04-12T10:16:00Z"
weight = 11928
keywords = [ "phonegap", "android" ]
aliases = [ "/questions/11928" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [android phonegap changeset create](/questions/11928/android-phonegap-changeset-create)

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
<span id="post-11928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11928-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am developing an android app using phonegap apis. I would like the app to to upload map data to osm using the osm apiv0.6. iam using the code below from localhost to create a changeset: function createChangeset(){</p>
<pre><code>    var xmlData = &#39;&lt;osm&gt;&lt;changeset&gt;&lt;tag k=&quot;created_by&quot; v=&quot;mappr&quot;/&gt;&lt;tag k=&quot;comment&quot; v=&quot;first upload&quot;/&gt;&lt;/changeset&gt;&lt;/osm&gt;&#39;;
&#10;    var url1 = &quot;http://api06.dev.openstreetmap.org/api/0.6/changeset/create&quot;;
&#10;$.ajax({
&#10;type:&quot;PUT&quot;,
username: &quot;debukali@gmail.com&quot;,
    password: &quot;lettersforme&quot;,
    url: url1,
data: xmlData,
&quot;error&quot;:function(xhr, textStatus, errorThrown)
{
if (xhr.status === 0) {
            alert(&#39;Not connect.\n Verify Network.&#39;);
        } else if (xhr.status == 404) {
            alert(&#39;Requested page not found. [404]&#39;);
        } else if (xhr.status == 500) {
            alert(&#39;Internal Server Error [500].&#39;);
        } else if (textStatus === &#39;parsererror&#39;) {
            alert(&#39;Requested JSON parse failed.&#39;);
        } else if (textStatus === &#39;timeout&#39;) {
            alert(&#39;Time out error.&#39;);
        } else if (textStatus === &#39;abort&#39;) {
            alert(&#39;Ajax request aborted.&#39;);
        } else {
            alert(&#39;Uncaught Error.\n&#39; + xhr.responseText);
        }
},
&#10;&quot;success&quot;:function(data)
{
     alert(&quot;Success: &quot;+data);
//$(&quot;#openingmessage&quot;).css(&quot;background&quot;,&quot;yellow&quot;).html(data);
}
});
    }</code></pre>
<p>Above code returns alert with success but the data is not shown.</p>
<p>Please show how to make changeset creation calls to osm api v0.6 in jquery or phonegap?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-phonegap" rel="tag" title="see questions tagged &#39;phonegap&#39;">phonegap</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '12, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/92ceae9166d1d984335264f68179ace6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidSerene&#39;s gravatar image" />
<p><span>DavidSerene</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidSerene has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11928" class="comments-container">
&#10;</div>
<div id="comment-tools-11928" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11928-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

