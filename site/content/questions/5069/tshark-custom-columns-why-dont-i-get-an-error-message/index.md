+++
type = "question"
title = "Tshark custom columns: Why don&#x27;t I get an error message?"
description = '''Correct syntax: $ tshark -r test.pcap -R &quot;frame.number&amp;lt;6&quot; -o column.format:&quot;&quot;No.&quot;,&quot;%m&quot;, &quot;tcp.port&quot;, &quot;%Cus:tcp.port&quot;, &quot;udp.port&quot;, &quot;%Cus:udp.port&quot;&quot;  1 55556,53  2 53,55556  3 1685,80  4 80,1685  5 1685,80  I get an error message, when I make a typo: %Cu:udp.port (instead of %Cus:udp.port) $ tshark ...'''
date = "2011-07-16T00:41:00Z"
lastmod = "2011-07-16T12:45:00Z"
weight = 5069
keywords = [ "error", "tshark", "syntax" ]
aliases = [ "/questions/5069" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Tshark custom columns: Why don't I get an error message?](/questions/5069/tshark-custom-columns-why-dont-i-get-an-error-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5069-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5069-score" class="post-score" title="current number of votes">0</div><span id="post-5069-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>Correct syntax:
$ tshark -r test.pcap -R &quot;frame.number&lt;6&quot; -o column.format:&quot;&quot;No.&quot;,&quot;%m&quot;, &quot;tcp.port&quot;, &quot;%Cus:tcp.port&quot;, &quot;udp.port&quot;, &quot;%Cus:udp.port&quot;&quot;
  1  55556,53
  2  53,55556
  3 1685,80
  4 80,1685
  5 1685,80

I get an error message, when I make a typo: %Cu:udp.port (instead of %Cus:udp.port)
$ tshark -r test.pcap -R &quot;frame.number&lt;6&quot; -o column.format:&quot;&quot;No.&quot;,&quot;%m&quot;, &quot;tcp.port&quot;, &quot;%Cus:tcp.port&quot;, &quot;udp.port&quot;, &quot;%Cu:udp.port&quot;&quot;
tshark: Invalid -o flag &quot;column.format:No.,%m, tcp.port, %Cus:tcp.port, udp.port, %Cu:udp.port&quot;

Why don&#39;t I get messages for the following typo&#39;s?
$ tshark -r test.pcap -R &quot;frame.number&lt;6&quot; -o column.format:&quot;&quot;No.&quot;,&quot;%m&quot;, &quot;tcp.port&quot;, &quot;%Cus:tcp.port&quot;, &quot;udp.port&quot;, &quot;%Cust:udp.port&quot;&quot;
  1
  2
  3 1685,80
  4 80,1685
  5 1685,80

$ tshark -r test.pcap -R &quot;frame.number&lt;6&quot; -o column.format:&quot;&quot;No.&quot;,&quot;%m&quot;, &quot;tcp.port&quot;, &quot;%Cus:tcp.port&quot;, &quot;udp.port&quot;, &quot;%Custttttttttttttt:udp.port&quot;&quot;
  1
  2
  3 1685,80
  4 80,1685
  5 1685,80
</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-syntax" rel="tag" title="see questions tagged &#39;syntax&#39;">syntax</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '11, 00:41</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span></p></div></div><div id="comments-container-5069" class="comments-container"></div><div id="comment-tools-5069" class="comment-tools"></div><div class="clear"></div><div id="comment-5069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5071"></span>

<div id="answer-container-5071" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5071-score" class="post-score" title="current number of votes">2</div><span id="post-5071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="joke has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The bug is that <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/prefs.c?revision=37830&amp;view=markup#l2044">prefs.c:2044</a> and <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/prefs.c?revision=37830&amp;view=markup#l2069">prefs.c:2069</a> compare only the first few characters of <code>"%Custttttttttttttt"</code>, which match the expected string (<code>%Cus</code>):</p><pre><code>const gchar *cust_format = col_format_to_string(COL_CUSTOM);
size_t cust_format_len = strlen(cust_format);
//...
if (strncmp(col_l_elt-&gt;data, cust_format, cust_format_len) == 0) {
        cfmt-&gt;fmt      = g_strdup(cust_format);
        prefs_fmt      = g_strdup(col_l_elt-&gt;data);
        cust_format_info = g_strsplit(&amp;prefs_fmt[cust_format_len+1],&quot;:&quot;,3); /* add 1 for &#39;:&#39; */
        cfmt-&gt;custom_field = g_strdup(cust_format_info[0]);
//....</code></pre><p>If we add 1 to <code>cust_format_len</code>, the string comparison would include the null terminator in <code>cust_format</code>, which would cause the desired syntax error:</p><pre><code>if (strncmp(col_l_elt-&gt;data, cust_format, cust_format_len+1) == 0) {
//...</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '11, 03:28</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Jul '11, 03:30</strong> </span></p></div></div><div id="comments-container-5071" class="comments-container"><span id="5072"></span><div id="comment-5072" class="comment"><div id="post-5072-score" class="comment-score"></div><div class="comment-text"><p>I will file a bug.<br />
Thanks.</p></div><div id="comment-5072-info" class="comment-info"><span class="comment-age">(16 Jul '11, 04:18)</span> <span class="comment-user userinfo">joke</span></div></div><span id="5074"></span><div id="comment-5074" class="comment"><div id="post-5074-score" class="comment-score"></div><div class="comment-text"><p>Done:<br />
<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6131">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6131</a></p></div><div id="comment-5074-info" class="comment-info"><span class="comment-age">(16 Jul '11, 07:51)</span> <span class="comment-user userinfo">joke</span></div></div><span id="5075"></span><div id="comment-5075" class="comment"><div id="post-5075-score" class="comment-score"></div><div class="comment-text"><p>The bug is fixed.<br />
Thanks to Stig:<br />
Added a fix in revision 38064.<br />
Scheduled for 1.4.8 and 1.6.1.<br />
<br />
You can download automated build 38064 <a href="http://www.wireshark.org/download/automated/">here</a></p></div><div id="comment-5075-info" class="comment-info"><span class="comment-age">(16 Jul '11, 12:45)</span> <span class="comment-user userinfo">joke</span></div></div></div><div id="comment-tools-5071" class="comment-tools"></div><div class="clear"></div><div id="comment-5071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

