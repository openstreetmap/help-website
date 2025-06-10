+++
type = "question"
title = "[closed] Get XML results from Nominatim"
description = '''Hi guys, I&#x27;m trying to get search results from Nominatim in XML format. Here&#x27;s my javascript code: function requestToNominatim(){   xmlhttp = getXMLHttpRequest();  xmlhttp.onreadystatechange=function(){  if (xmlhttp.readyState==4 &amp;amp;&amp;amp; xmlhttp.status==200){  var response = xmlhttp.responseXML; ...'''
date = "2013-06-14T14:42:00Z"
lastmod = "2013-06-17T08:51:00Z"
weight = 23375
keywords = [ "xml", "search", "nominatim", "geocoding" ]
aliases = [ "/questions/23375" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Get XML results from Nominatim](/questions/23375/closed-get-xml-results-from-nominatim)

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
<span id="post-23375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23375-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys,</p>
<p>I'm trying to get search results from Nominatim in XML format. Here's my javascript code:</p>
<pre><code>function requestToNominatim(){
&#10;    xmlhttp = getXMLHttpRequest();
    xmlhttp.onreadystatechange=function(){
        if (xmlhttp.readyState==4 &amp;&amp; xmlhttp.status==200){
            var response = xmlhttp.responseXML;
            alert(response);
            }
    }
&#10;    var q = document.getElementById(&#39;q&#39;).value;
    xmlhttp.open(&quot;GET&quot;,&quot;http://localhost/nominatim/search.php?format=xml&amp;q=&quot; + q,true);
    xmlhttp.send(null);
}</code></pre>
<p>The alert displays "[object Document]". However, when I display "responseText" I get the xml... Do you have any idea about getting directly the XMLDocument from responseXML?</p>
<p>Thanks! Lucas</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jun '13, 14:42</strong></p>
<img src="https://secure.gravatar.com/avatar/4015aaa7dcb688fc988901e4caaac771?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kalu06&#39;s gravatar image" />
<p><span>Kalu06</span><br />
<span class="score" title="140 reputation points">140</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kalu06 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jun '13, 08:58</strong> </span></p>
</div>
</div>
<div id="comments-container-23375" class="comments-container">
<span id="23440"></span>
<div id="comment-23440" class="comment">
<div id="post-23440-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Finally, I ended up using JSON instead of XML. It's working as good and easier to manipulate.</p>
<p>Lucas</p>
</div>
<div id="comment-23440-info" class="comment-info">
<span class="comment-age">(17 Jun '13, 08:51)</span> <span class="comment-user userinfo">Kalu06</span>
</div>
</div>
</div>
<div id="comment-tools-23375" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23375-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

