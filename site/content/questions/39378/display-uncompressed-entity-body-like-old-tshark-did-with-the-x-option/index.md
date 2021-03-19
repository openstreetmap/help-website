+++
type = "question"
title = "Display &quot;Uncompressed entity body&quot; like old tshark did with the -x option"
description = '''In tshark 1.6.7 the command tshark -i lo -x -R &#x27;http.response.code == 302&#x27; -l  resulted in an output like the following:  26.047812 127.0.0.1 -&amp;gt; 127.0.0.1 HTTP 798 HTTP/1.1 302 Found (text/html)  Frame (798 bytes):  0000 00 00 00 00 00 00 00 00 00 00 00 00 08 00 45 00 ..............E. 0010 03 10 ...'''
date = "2015-01-24T03:18:00Z"
lastmod = "2015-01-27T17:34:00Z"
weight = 39378
keywords = [ "tshark" ]
aliases = [ "/questions/39378" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Display "Uncompressed entity body" like old tshark did with the -x option](/questions/39378/display-uncompressed-entity-body-like-old-tshark-did-with-the-x-option)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39378-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39378-score" class="post-score" title="current number of votes">0</div><span id="post-39378-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In tshark 1.6.7 the command</p><pre><code>tshark -i lo -x -R &#39;http.response.code == 302&#39; -l</code></pre><p>resulted in an output like the following:</p><pre><code> 26.047812    127.0.0.1 -&gt; 127.0.0.1    HTTP 798 HTTP/1.1 302 Found  (text/html)

Frame (798 bytes):

0000  00 00 00 00 00 00 00 00 00 00 00 00 08 00 45 00   ..............E.
0010  03 10 1a 6a 40 00 40 06 1f 7c 7f 00 00 01 7f 00   [email protected]@..|......
0020  00 01 00 50 c4 51 20 88 1b 52 89 29 63 e3 80 18   ...P.Q ..R.)c...
0030  02 00 01 05 00 00 01 01 08 0a 00 1d 01 41 00 1d   .............A..
0040  01 3b 48 54 54 50 2f 31 2e 31 20 33 30 32 20 46   .;HTTP/1.1 302 F
0050  6f 75 6e 64 0d 0a 44 61 74 65 3a 20 4d 6f 6e 2c   ound..Date: Mon,
[many more lines like this ...]

Uncompressed entity body (1069 bytes):

0000  3c 70 72 65 20 63 6c 61 73 73 3d 27 78 64 65 62   fpre class=&#39;xdeb
0010  75 67 2d 76 61 72 2d 64 75 6d 70 27 20 64 69 72   ug-var-dump&#39; dir
0020  3d 27 6c 74 72 27 3e 0a 3c 62 3e 61 72 72 61 79   =&#39;ltr&#39;&gt;.&lt;b&gt;array
0030  3c 2f 62 3e 0a 20 20 27 61 72 74 4e 61 6d 65 27   &lt;/b&gt;.  &#39;varnamee&#39;
[many more lines like this ...]</code></pre><p>Is it possible to get that output with tshark 1.12.3 as well? Especially the part that begins with "Uncompressed entity body" is important for me because I pipe tshark's output to a script which converts that part into a readable text.</p><p>I read the release notes at <a href="https://www.wireshark.org/docs/relnotes/wireshark-1.10.0.html">https://www.wireshark.org/docs/relnotes/wireshark-1.10.0.html</a>. They suggest using -Px instead of x. So my current command looks like</p><pre><code>tshark -i lo -Px -Y &#39;http.response.code == 302&#39; -l</code></pre><p>But that command does not show the uncompressed entity body.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '15, 03:18</strong></p><img src="https://secure.gravatar.com/avatar/d35774ec5eb4bae1cb17de194e84a1ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miachino&#39;s gravatar image" /><p><span>miachino</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miachino has no accepted answers">0%</span></p></div></div><div id="comments-container-39378" class="comments-container"></div><div id="comment-tools-39378" class="comment-tools"></div><div class="clear"></div><div id="comment-39378-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39380"></span>

<div id="answer-container-39380" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39380-score" class="post-score" title="current number of votes">2</div><span id="post-39380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="miachino has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The command line <code>tshark -r input.pcapng -x -l -Y 'http.response.code == 200'</code> works for me with tshark 1.12.3, I get the output below:</p><pre><code>Frame (792 bytes):
0000  74 d0 2b 9e 2d 54 c0 c1 c0 78 70 c7 08 00 45 00   t.+.-T...xp...E.
...
0310  00 0d 0a 30 0d 0a 0d 0a                           ...0....
Reassembled TCP (5094 bytes):
0000  48 54 54 50 2f 31 2e 31 20 32 30 30 20 4f 4b 0d   HTTP/1.1 200 OK.
...
13e0  0a 30 0d 0a 0d 0a                                 .0....
De-chunked entity body (4686 bytes):
0000  1f 8b 08 00 00 00 00 00 00 03 cd 5b 6d 73 1b 37   ...........[ms.7
...
1240  fb 4e cf f5 ff 00 7d 6e 14 c7 ec 44 00 00         .N....}n...D..
Uncompressed entity body (17644 bytes):
0000  76 61 72 20 63 75 72 5f 74 6f 70 69 63 5f 69 64   var cur_topic_id
...</code></pre><p>Can you post a small capture that exhibits the problem somewhere public, e.g. <a href="http:\cloudshark.org">Cloudshark</a>, Google Drive, Dropbox?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '15, 04:39</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-39380" class="comments-container"><span id="39383"></span><div id="comment-39383" class="comment"><div id="post-39383-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span> You are refering to a situation in which a previously written capture file is read. In that case my output is similar to yours. What I am looking for is a solution with live capturing. The command that I mentioned could be entered on the command line and each time a package with http response code 302 is found it is written into the the terminal immediately. Is that still possible? Thanx for your answer.</p></div><div id="comment-39383-info" class="comment-info"><span class="comment-age">(24 Jan '15, 06:23)</span> <span class="comment-user userinfo">miachino</span></div></div><span id="39390"></span><div id="comment-39390" class="comment"><div id="post-39390-score" class="comment-score"></div><div class="comment-text"><p>Interesting, I tried it on a live capture redirecting the output to a file, <code>tshark -i 4 -x -l -Y 'http.response.code == 200' &gt; c:\temp\xx.txt</code> and got the expected output.</p><p>If I just print to the console though, I don't see the "headers" at the start of each part of the output. Very odd, nor do I see the entity body in the hex.</p></div><div id="comment-39390-info" class="comment-info"><span class="comment-age">(25 Jan '15, 09:24)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="39401"></span><div id="comment-39401" class="comment"><div id="post-39401-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span> Thanx for testing. In my case redirecting tshark's output to a file or printing the output directly to the terminal doesn't make a difference. I do not get the part "Uncompressed entity body" in both cases. Does that mean that it is not possible anymore to get the uncompressed entity body with tshark in a live capture? (I use arch linux.)</p></div><div id="comment-39401-info" class="comment-info"><span class="comment-age">(26 Jan '15, 08:04)</span> <span class="comment-user userinfo">miachino</span></div></div><span id="39402"></span><div id="comment-39402" class="comment"><div id="post-39402-score" class="comment-score"></div><div class="comment-text"><p>It must be possible as I managed it (on Windows) when redirecting to a file. In your intended use you are redirecting the output somewhere though?</p></div><div id="comment-39402-info" class="comment-info"><span class="comment-age">(26 Jan '15, 08:21)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="39403"></span><div id="comment-39403" class="comment"><div id="post-39403-score" class="comment-score"></div><div class="comment-text"><p>just a thought, in the default Wireshark profile you do have all the http dissector reassemble options enabled, along with "Uncompress entity bodies" and the tcp dissector option "Allow subdissector to reassemble TCP streams".</p></div><div id="comment-39403-info" class="comment-info"><span class="comment-age">(26 Jan '15, 08:35)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="39404"></span><div id="comment-39404" class="comment not_top_scorer"><div id="post-39404-score" class="comment-score"></div><div class="comment-text"><p>You can check the prefs used in your tshark invocation by using:</p><pre><code>tshark -G currentprefs | &lt;filter for &quot;http.&quot;&gt;</code></pre><p>replacing the filter method string with whatever is appropriate for your environment. I get:</p><pre><code>#http.desegment_headers: TRUE
#http.desegment_body: TRUE
#http.dechunk_body: TRUE
#http.decompress_body: TRUE
#http.tcp.port: 80,3128,3132,5985,8080,8088,11371,1900,2869,2710
#http.ssl.port: 443</code></pre><p>The other one to check is "tcp.desgment_tcp_streams", I have:</p><pre><code>#tcp.desegment_tcp_streams: TRUE</code></pre></div><div id="comment-39404-info" class="comment-info"><span class="comment-age">(26 Jan '15, 08:50)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="39405"></span><div id="comment-39405" class="comment not_top_scorer"><div id="post-39405-score" class="comment-score"></div><div class="comment-text"><p>There's a site <a href="http://httpbin/org">httpbin.org</a> that allows you to test certain http responses. Using the request <code>http://httpbin.org/gzip</code> and a tshark capture line of:</p><pre><code>ts -i 2 -x -l -f &quot;host httpbin.org&quot; -Y &#39;http.response.code == 200&#39;</code></pre><p>I see the uncompressed data:</p><p><code> Capturing on 'Ethernet'                                                Frame (670 bytes):                                                     0000  f8 b1 56 e1 c0 8b 00 d0 cf 03 7c 30 08 00 45 80   ..V.......|0..E. 0010  02 90 f7 93 40 00 2f 06 ab 00 36 af de f6 0a 9e   [email protected]/...6..... 0020  86 10 00 50 d0 58 f5 27 83 4c 28 be 87 ad 50 18   ...P.X.'.L(...P. 0030  01 12 f1 5f 00 00 48 54 54 50 2f 31 2e 31 20 32   ..._..HTTP/1.1 2 0040  30 30 20 4f 4b 0d 0a 53 65 72 76 65 72 3a 20 6e   00 OK..Server: n 0050  67 69 6e 78 0d 0a 44 61 74 65 3a 20 4d 6f 6e 2c   ginx..Date: Mon, 0060  20 32 36 20 4a 61 6e 20 32 30 31 35 20 31 37 3a    26 Jan 2015 17: 0070  31 31 3a 30 38 20 47 4d 54 0d 0a 43 6f 6e 74 65   11:08 GMT..Conte ... 0280  f3 88 66 49 c5 63 2e 4a ac 6f b4 2e f6 1c 4c bb   ..fI.c.J.o....L. 0290  be d5 b8 37 7e 00 54 a8 81 25 1b 02 00 00         ...7~.T..%.... Uncompressed entity body (539 bytes): 0000  7b 0a 20 20 22 67 7a 69 70 70 65 64 22 3a 20 74   {.  "gzipped": t 0010  72 75 65 2c 20 0a 20 20 22 68 65 61 64 65 72 73   rue, .  "headers 0020  22 3a 20 7b 0a 20 20 20 20 22 41 63 63 65 70 74   ": {.    "Accept ...</code></p></div><div id="comment-39405-info" class="comment-info"><span class="comment-age">(26 Jan '15, 09:15)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="39432"></span><div id="comment-39432" class="comment not_top_scorer"><div id="post-39432-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span> Yes, I used tshark 1.6.7 in a command like the following:</p><p>tshark -i lo -x -R 'http.response.code == 302' -l | scriptThatParsesTsharksOutput.php</p><p>That does not work anymore because my php script expects the input that was delivered by tshark 1.6.7.</p><p>To your other question: I didn't have wireshark installed, only tshark. Do settings in wireshark effect how tshark works?</p><p>Because of your question I installed wireshark but I do not have a default profile I think. In wireshark I click Edit -&gt; Configuration Profiles. In the popup window I see three profiles: Default, Bluetooth and Classic. For each profile a directory name is given. For the profile "Default" that directory name is ~/.wireshark/profiles but that directory does not exist. I only have the directory ~/.wireshark with the two files recent and recent_common. That's why I said that I think that I do not have a default profile.</p></div><div id="comment-39432-info" class="comment-info"><span class="comment-age">(27 Jan '15, 03:03)</span> <span class="comment-user userinfo">miachino</span></div></div><span id="39433"></span><div id="comment-39433" class="comment not_top_scorer"><div id="post-39433-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span> Ah, I did not see your last two comments before I wrote my comment because they where hidden and only visible after clicking "show 2 more comments". I will check that.</p></div><div id="comment-39433-info" class="comment-info"><span class="comment-age">(27 Jan '15, 03:09)</span> <span class="comment-user userinfo">miachino</span></div></div><span id="39435"></span><div id="comment-39435" class="comment not_top_scorer"><div id="post-39435-score" class="comment-score"></div><div class="comment-text"><p>I just repeated my test to <a href="http://httpbin.org/gzip,">http://httpbin.org/gzip,</a> piping tshark output to another program and got the expected text.</p><p>Can you try that?</p></div><div id="comment-39435-info" class="comment-info"><span class="comment-age">(27 Jan '15, 03:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="39445"></span><div id="comment-39445" class="comment not_top_scorer"><div id="post-39445-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span> Testing with that website was a very good idea because that test showed me that I indeed get the expected result as well. The reason why I did not get the part "Uncompressed entity body" was because I performed my tests with a page, that was very short and in that case the Apache web server does not compress the response as I found out at <a href="http://httpd.apache.org/docs/trunk/upgrading.html.">http://httpd.apache.org/docs/trunk/upgrading.html.</a> There I found the note: "mod_deflate will now skip compression if it knows that the size overhead added by the compression is larger than the data to be compressed." That was the case in my situation. So there simply was no compressed part. Thank you very much for your kind help and for your patience.</p><p>Now I have another related question but I guess that it's better to ask that in a separate question.</p></div><div id="comment-39445-info" class="comment-info"><span class="comment-age">(27 Jan '15, 17:34)</span> <span class="comment-user userinfo">miachino</span></div></div></div><div id="comment-tools-39380" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-39380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

