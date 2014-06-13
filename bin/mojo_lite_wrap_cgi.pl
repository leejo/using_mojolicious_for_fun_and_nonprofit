#!/usr/bin/env perl

use Mojolicious::Lite;
use Mojolicious::Plugin::CGI;

plugin CGI => [ '/hello_world' => "hello_world.cgi" ];

app->start;
