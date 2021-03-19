+++
type = "question"
title = "where does ssl_print_data() display its output?"
description = '''I&#x27;ve apiece of an external dissector code where several calls have been made to the function ssl_print_data. I&#x27;m not able to find out where the arguments passed to this function are printed out! I found it defined in the file packet-ssl-utils.c as the following:  void ssl_print_data(const gchar* nam...'''
date = "2014-08-01T14:04:00Z"
lastmod = "2014-11-10T09:59:00Z"
weight = 35075
keywords = [ "debug", "ssl_print_data", "dissector", "wireshark" ]
aliases = [ "/questions/35075" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [where does ssl\_print\_data() display its output?](/questions/35075/where-does-ssl_print_data-display-its-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35075-score" class="post-score" title="current number of votes">0</div><span id="post-35075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've apiece of an external dissector code where several calls have been made to the function <strong>ssl_print_data</strong>. I'm not able to find out where the arguments passed to this function are printed out!</p><p>I found it defined in the file packet-ssl-utils.c as the following:</p><pre><code>void
ssl_print_data(const gchar* name, const guchar* data, size_t len)
{
    size_t i;
    if (!ssl_debug_file)
        return;
    fprintf(ssl_debug_file,&quot;%s[%d]:\n&quot;,name, (int) len);
    for (i=0; i&lt; len; i++) {
        if ((i&gt;0) &amp;&amp; (i%16 == 0))
            fprintf(ssl_debug_file,&quot;\n&quot;);
        fprintf(ssl_debug_file,&quot;%.2x &quot;,data[i]&amp;255);
    }
    fprintf(ssl_debug_file,&quot;\n&quot;);
}</code></pre><p>I also found <strong>ssl_debug_file</strong> is defined in the same file as the following</p><pre><code>static FILE* ssl_debug_file=NULL;

void
ssl_set_debug(char* name)
{
    static gint debug_file_must_be_closed;
    gint use_stderr;
    debug_file_must_be_closed = 0;
    use_stderr = name?(strcmp(name, SSL_DEBUG_USE_STDERR) == 0):0;

    if (debug_file_must_be_closed)
        fclose(ssl_debug_file);
    if (use_stderr)
        ssl_debug_file = stderr;
    else if (!name || (strcmp(name, &quot;&quot;) ==0))
        ssl_debug_file = NULL;
    else
        ssl_debug_file = ws_fopen(name, &quot;w&quot;);
    if (!use_stderr &amp;&amp; ssl_debug_file)
        debug_file_must_be_closed = 1;
}</code></pre><p>It is not printing into console as I was not able to find any messages related to this specific function there. Should I create the <strong>ssl_debug_file</strong> somewhere ? If it is already exist where is it?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-debug" rel="tag" title="see questions tagged &#39;debug&#39;">debug</span> <span class="post-tag tag-link-ssl_print_data" rel="tag" title="see questions tagged &#39;ssl_print_data&#39;">ssl_print_data</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '14, 14:04</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p><span>flora</span><br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Aug '14, 14:30</strong> </span></p></div></div><div id="comments-container-35075" class="comments-container"></div><div id="comment-tools-35075" class="comment-tools"></div><div class="clear"></div><div id="comment-35075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35100"></span>

<div id="answer-container-35100" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35100-score" class="post-score" title="current number of votes">0</div><span id="post-35100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flora has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can define the SSL debug file here</p><blockquote><p>Edit -&gt; Preferences -&gt; Protocols -&gt; SSL -&gt; SSL debug file</p></blockquote><p>Please choose any existing file with the File dialog widget (Browse... button), or simply enter the file name.</p><p>If you want the messages to go to STDERR, please enter <strong>-</strong> (minus) as the file name.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '14, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-35100" class="comments-container"><span id="37734"></span><div id="comment-37734" class="comment"><div id="post-37734-score" class="comment-score"></div><div class="comment-text"><p>Thanks! This solves my problem.</p></div><div id="comment-37734-info" class="comment-info"><span class="comment-age">(10 Nov '14, 09:59)</span> <span class="comment-user userinfo">flora</span></div></div></div><div id="comment-tools-35100" class="comment-tools"></div><div class="clear"></div><div id="comment-35100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

