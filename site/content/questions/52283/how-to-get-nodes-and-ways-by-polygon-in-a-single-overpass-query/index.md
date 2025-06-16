+++
type = "question"
title = "How to get nodes and ways by polygon in a single Overpass query"
description = '''How can I get all the nodes and ways within some polygon in a single Overpass API query? For example, I can get all the ways like this;out;) and all the nodes like this.  But how might I combine these HTTP GET requests into a single query?'''
date = "2016-09-28T17:03:00Z"
lastmod = "2016-09-29T03:18:00Z"
weight = 52283
keywords = [ "overpassapi", "overpass", "openstreetmap", "api", "overpass-turbo" ]
aliases = [ "/questions/52283" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to get nodes and ways by polygon in a single Overpass query](/questions/52283/how-to-get-nodes-and-ways-by-polygon-in-a-single-overpass-query)

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
<span id="post-52283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52283-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I get all the nodes and ways within some polygon in a single Overpass API query? For example, I can get all the ways <a href="http://www.overpass-api.de/api/interpreter?data=%5Bout:json%5D%5Btimeout:360%5D;way%5B" title="highway&quot;](poly:&quot;40.46125250000001 -80.2224771185185 40.461511 -80.221738 40.461597999999995 -80.22151 40.461695999999996 -80.221293 40.46181 -80.22108899999999 40.461894 -80.220968 40.461939 -80.220902 40.462081 -80.220732 40.462235 -80.220581 40.462384 -80.220462 40.462399 -80.220451 40.462568 -80.220342 40.462783 -80.22024499999999 40.463015 -80.220173 40.463124 -80.220146 40.463138 -80.220143 40.463311 -80.220118 40.463409999999996 -80.220111 40.463605 -80.220106 40.463873 -80.220109 40.463876 -80.21988999999999 40.463884 -80.21977 40.463902999999995 -80.21967099999999 40.463932 -80.21958599999999 40.463986 -80.21949 40.464034 -80.21942 40.463864 -80.21931699999999 40.463708 -80.219253 40.46384 -80.219183 40.464085 -80.219376 40.464422 -80.21937 40.465002999999996 -80.219248 40.466426 -80.218577 40.46763 -80.218542 40.470379 -80.21951 40.470436 -80.219543 40.470755 -80.219729 40.470566999999996 -80.220051 40.470346 -80.220401 40.470424 -80.220447 40.47092 -80.220839 40.471806 -80.221527 40.471931 -80.221639 40.472075 -80.220137 40.472207999999995 -80.21859099999999 40.472282 -80.218097 40.472384 -80.217075 40.472552 -80.215248 40.472558 -80.214581 40.472543 -80.214029 40.472515 -80.213465 40.472432999999995 -80.212988 40.47229 -80.212409 40.472122 -80.21175199999999 40.471914 -80.211146 40.471581 -80.21046 40.471134 -80.209606 40.470575 -80.208596 40.470191 -80.20788399999999 40.469651999999996 -80.206862 40.469166 -80.205924 40.468755 -80.204903 40.46845 -80.203957 40.468272999999996 -80.202919 40.467835 -80.200237 40.467863 -80.200144 40.467856 -80.200133 40.467835 -80.2001 40.467828999999995 -80.20009 40.467821 -80.200075 40.467805999999996 -80.20003 40.467791 -80.200019 40.467743 -80.199783 40.467571 -80.199142 40.467464 -80.198837 40.467411999999996 -80.19867599999999 40.467304 -80.19841 40.467281 -80.19836099999999 40.467213 -80.198219 40.466988 -80.197769 40.466682 -80.19725799999999 40.466553999999995 -80.197057 40.466418999999995 -80.196861 40.466122 -80.19649 40.465945999999995 -80.196281 40.465793999999995 -80.196114 40.465446 -80.195801 40.465095999999996 -80.195492 40.464763 -80.195225 40.464016 -80.194627 40.46371 -80.194389 40.462249 -80.19318 40.46125250000001 -80.19234783738503 40.46125250000001 -80.2224771185185">like this</a>;out;) and all the nodes <a href="http://www.overpass-api.de/api/interpreter?data=%5Bout:json%5D%5Btimeout:360%5D;way%5B%22highway%22%5D(poly:%2240.46125250000001%20-80.2224771185185%2040.461511%20-80.221738%2040.461597999999995%20-80.22151%2040.461695999999996%20-80.221293%2040.46181%20-80.22108899999999%2040.461894%20-80.220968%2040.461939%20-80.220902%2040.462081%20-80.220732%2040.462235%20-80.220581%2040.462384%20-80.220462%2040.462399%20-80.220451%2040.462568%20-80.220342%2040.462783%20-80.22024499999999%2040.463015%20-80.220173%2040.463124%20-80.220146%2040.463138%20-80.220143%2040.463311%20-80.220118%2040.463409999999996%20-80.220111%2040.463605%20-80.220106%2040.463873%20-80.220109%2040.463876%20-80.21988999999999%2040.463884%20-80.21977%2040.463902999999995%20-80.21967099999999%2040.463932%20-80.21958599999999%2040.463986%20-80.21949%2040.464034%20-80.21942%2040.463864%20-80.21931699999999%2040.463708%20-80.219253%2040.46384%20-80.219183%2040.464085%20-80.219376%2040.464422%20-80.21937%2040.465002999999996%20-80.219248%2040.466426%20-80.218577%2040.46763%20-80.218542%2040.470379%20-80.21951%2040.470436%20-80.219543%2040.470755%20-80.219729%2040.470566999999996%20-80.220051%2040.470346%20-80.220401%2040.470424%20-80.220447%2040.47092%20-80.220839%2040.471806%20-80.221527%2040.471931%20-80.221639%2040.472075%20-80.220137%2040.472207999999995%20-80.21859099999999%2040.472282%20-80.218097%2040.472384%20-80.217075%2040.472552%20-80.215248%2040.472558%20-80.214581%2040.472543%20-80.214029%2040.472515%20-80.213465%2040.472432999999995%20-80.212988%2040.47229%20-80.212409%2040.472122%20-80.21175199999999%2040.471914%20-80.211146%2040.471581%20-80.21046%2040.471134%20-80.209606%2040.470575%20-80.208596%2040.470191%20-80.20788399999999%2040.469651999999996%20-80.206862%2040.469166%20-80.205924%2040.468755%20-80.204903%2040.46845%20-80.203957%2040.468272999999996%20-80.202919%2040.467835%20-80.200237%2040.467863%20-80.200144%2040.467856%20-80.200133%2040.467835%20-80.2001%2040.467828999999995%20-80.20009%2040.467821%20-80.200075%2040.467805999999996%20-80.20003%2040.467791%20-80.200019%2040.467743%20-80.199783%2040.467571%20-80.199142%2040.467464%20-80.198837%2040.467411999999996%20-80.19867599999999%2040.467304%20-80.19841%2040.467281%20-80.19836099999999%2040.467213%20-80.198219%2040.466988%20-80.197769%2040.466682%20-80.19725799999999%2040.466553999999995%20-80.197057%2040.466418999999995%20-80.196861%2040.466122%20-80.19649%2040.465945999999995%20-80.196281%2040.465793999999995%20-80.196114%2040.465446%20-80.195801%2040.465095999999996%20-80.195492%2040.464763%20-80.195225%2040.464016%20-80.194627%2040.46371%20-80.194389%2040.462249%20-80.19318%2040.46125250000001%20-80.19234783738503%2040.46125250000001%20-80.2224771185185%22);%3E;out;">like this</a>.</p>
<p>But how might I combine these HTTP GET requests into a single query?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Sep '16, 17:03</strong></p>
<img src="https://secure.gravatar.com/avatar/8eb28ad933ae655db57b6c6b8563eb67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gboeing&#39;s gravatar image" />
<p><span>gboeing</span><br />
<span class="score" title="136 reputation points">136</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gboeing has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52283" class="comments-container">
&#10;</div>
<div id="comment-tools-52283" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52283-form-container" class="comment-form-container">
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

<span id="52289"></span>

<div id="answer-container-52289" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52289-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gboeing has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Take a look at the union operator:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Union">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Union</a></p>
<p>You will have to repeat the poly statement. Here's the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_polygon_.28poly.29">poly example</a> from the docs wrapped in a union:</p>
<pre><code>(
  node(poly:&quot;50.7 7.1 50.7 7.2 50.75 7.15&quot;);
  way(poly:&quot;50.7 7.1 50.7 7.2 50.75 7.15&quot;);
  rel(poly:&quot;50.7 7.1 50.7 7.2 50.75 7.15&quot;);
);</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '16, 22:04</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-52289" class="comments-container">
<span id="52293"></span>
<div id="comment-52293" class="comment">
<div id="post-52293-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, yes, the wrapping parentheses were what I needed.</p>
</div>
<div id="comment-52293-info" class="comment-info">
<span class="comment-age">(29 Sep '16, 03:18)</span> <span class="comment-user userinfo">gboeing</span>
</div>
</div>
</div>
<div id="comment-tools-52289" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52289-form-container" class="comment-form-container">
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

