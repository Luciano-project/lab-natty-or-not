from flask import Flask, request, redirect, url_for, render_template
from flask_restful import Api
from config import REPLICATE_API_KEY, os
import replicate
import requests
import json

