+++
type = "question"
title = "I want to use Main/Overpass API for retrieving data in c++ program."
description = '''I want my program to have the street&#x27;s and building&#x27;s data in xml format. But I have no idea how to start this project. I am new to using api&#x27;s and reading about the api does not tell me how do I actually write api call in my c++ code and retrieve the data. What sources should I refer to write a sim...'''
date = "2012-12-24T06:25:00Z"
lastmod = "2012-12-24T13:40:00Z"
weight = 18684
keywords = [ "overpass", "c++", "newbie", "tutorial", "osm" ]
aliases = [ "/questions/18684" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [I want to use Main/Overpass API for retrieving data in c++ program.](/questions/18684/i-want-to-use-mainoverpass-api-for-retrieving-data-in-c-program)

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
<span id="post-18684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18684-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want my program to have the street's and building's data in xml format.</p>
<p>But I have no idea how to start this project. I am new to using api's and reading about the api does not tell me how do I <strong>actually write api call in my c++ code and retrieve the data.</strong> What sources should I refer to write a simple program to say :</p>
<pre><code>                              &quot;retrieve bounding box xml file in osm map&quot;</code></pre>
<p>All queries are on wiki page, but where to write this queries and required setup for starting with this api usage is evasive.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-c++" rel="tag" title="see questions tagged &#39;c++&#39;">c++</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-tutorial" rel="tag" title="see questions tagged &#39;tutorial&#39;">tutorial</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Dec '12, 06:25</strong></p>
<img src="https://secure.gravatar.com/avatar/bd411afe7563961a31610b5f4d40dfd3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anubha&#39;s gravatar image" />
<p><span>Anubha</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anubha has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Dec '12, 06:27</strong> </span></p>
</div>
</div>
<div id="comments-container-18684" class="comments-container">
<span id="18691"></span>
<div id="comment-18691" class="comment">
<div id="post-18691-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Implementing the API call in your project is <em>very</em> programming/scripting language-specific and hasn't much to do with OSM.</p>
</div>
<div id="comment-18691-info" class="comment-info">
<span class="comment-age">(24 Dec '12, 11:57)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-18684" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18684-form-container" class="comment-form-container">
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

<span id="18690"></span>

<div id="answer-container-18690" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18690-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-18690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Anubha has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a minimal working example in plain C/C++ with only minimal error checking and no response processing:</p>
<pre><code>#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;vector&gt;
#include &lt;cstdio&gt;
#include &lt;arpa/inet.h&gt;
#include &lt;sys/socket.h&gt;
&#10;const std::string host  = &quot;81.19.81.199&quot;; // IP of overpass.osm.rambler.ru
const int port          = 80;
const std::string query = &quot;GET /cgi/interpreter?data=node%5Bname%3DGielgen%5D%3Bout%3B HTTP/1.1\r\n&quot;
                          &quot;Host: overpass.osm.rambler.ru\r\n&quot;
                          &quot;User-Agent: SteveC\r\n&quot;
                          &quot;Accept: */*\r\n&quot;
                          &quot;Connection: close\r\n&quot;
                          &quot;\r\n&quot;;
&#10;int main(int argc, char* argv[]) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) {
        perror(&quot;error opening socket&quot;); return -1;
    }
&#10;    struct sockaddr_in sin;
    sin.sin_port = htons(port);
    sin.sin_addr.s_addr = inet_addr(host.c_str());
    sin.sin_family = AF_INET;
&#10;    if (connect(sock, (struct sockaddr *)&amp;sin, sizeof(sin)) == -1) {
        perror(&quot;error connecting to host&quot;); return -1;
    }
&#10;    const int query_len = query.length() + 1; // trailing &#39;\0&#39;
    if (send(sock, query.c_str(), query_len, 0) != query_len) {
        perror(&quot;error sending query&quot;); return -1;
    }
&#10;    const int buf_size = 1024 * 1024;
    while (true) {
        std::vector&lt;char&gt; buf(buf_size, &#39;\0&#39;);
        const int recv_len = recv(sock, &amp;buf[0], buf_size - 1, 0);
&#10;        if (recv_len == -1) {
            perror(&quot;error receiving response&quot;); return -1;
        } else if (recv_len == 0) {
            std::cout &lt;&lt; std::endl; break;
        } else {
            std::cout &lt;&lt; &amp;buf[0];
        }
    }
&#10;    return 0;
}</code></pre>
<p>Example output:</p>
<pre><code>HTTP/1.1 200 OK
Server: nginx/1.0.9
Date: Mon, 24 Dec 2012 11:45:34 GMT
Content-Type: application/osm3s+xml
Connection: close
Content-Length: 1893
Access-Control-Allow-Origin: *
&#10;&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;osm version=&quot;0.6&quot; generator=&quot;Overpass API&quot;&gt;
&lt;note&gt;The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.&lt;/note&gt;
&lt;meta osm_base=&quot;2012-12-24T11:44:01Z&quot;/&gt;
&#10;  &lt;node id=&quot;371597317&quot; lat=&quot;50.7412721&quot; lon=&quot;7.1927120&quot;&gt;
    &lt;tag k=&quot;is_in&quot; v=&quot;Bonn,Regierungsbezirk Köln,Nordrhein-Westfalen,Bundesrepublik Deutschland,Europe&quot;/&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Gielgen&quot;/&gt;
    &lt;tag k=&quot;place&quot; v=&quot;suburb&quot;/&gt;
  &lt;/node&gt;
&#10;[cropped]
&#10;&lt;/osm&gt;</code></pre>
<p>I strongly suggest using a third-party library for the network/HTTP code and you will probably also want to use a third-party library for parsing the XML/JSON/whatever response.</p>
<p>A much simpler option is to use a scripting language like Python, Ruby, or - if you like camels - Perl.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Dec '12, 11:51</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-18690" class="comments-container">
<span id="18692"></span>
<div id="comment-18692" class="comment">
<div id="post-18692-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you again (again as you replied in stackOverflow), I ran the code, and it worked, its first time I connected to an internet server. Will make project in which user will be able to ride a car in any part of world he/she wishes, buildings will be mostly random.</p>
</div>
<div id="comment-18692-info" class="comment-info">
<span class="comment-age">(24 Dec '12, 12:35)</span> <span class="comment-user userinfo">Anubha</span>
</div>
</div>
<span id="18693"></span>
<div id="comment-18693" class="comment">
<div id="post-18693-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah, I didn't remember your username :)</p>
</div>
<div id="comment-18693-info" class="comment-info">
<span class="comment-age">(24 Dec '12, 13:40)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-18690" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18690-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18685"></span>

<div id="answer-container-18685" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18685-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-18685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>An API call is done via HTTP, so your program needs to open a network connection. Libraries for C++ that do so are discussed for example <a href="http://stackoverflow.com/questions/1011339/how-do-you-make-a-http-request-with-c">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Dec '12, 07:08</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-18685" class="comments-container">
<span id="18686"></span>
<div id="comment-18686" class="comment">
<div id="post-18686-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Also checkout <a href="https://wiki.openstreetmap.org/wiki/Osmium/Architecture#OSM_Files">file handling in Osmium</a>.</p>
</div>
<div id="comment-18686-info" class="comment-info">
<span class="comment-age">(24 Dec '12, 07:20)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="18687"></span>
<div id="comment-18687" class="comment">
<div id="post-18687-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks, any code samples with simple osm api calls would be really helpful.</p>
</div>
<div id="comment-18687-info" class="comment-info">
<span class="comment-age">(24 Dec '12, 08:14)</span> <span class="comment-user userinfo">Anubha</span>
</div>
</div>
</div>
<div id="comment-tools-18685" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18685-form-container" class="comment-form-container">
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

